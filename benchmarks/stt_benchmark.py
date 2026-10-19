"""
STT benchmark for BE-03: compares LOCAL speech-to-text models on kk/ru/en/mixed audio.

Folder layout:
    benchmarks/data/<lang>/<name>.<wav|mp3|ogg|m4a>   # lang: kk, ru, en, mixed
    benchmarks/data/<lang>/<name>.txt                  # reference transcript

Usage:
    pip install faster-whisper transformers torch librosa jiwer
    python benchmarks/stt_benchmark.py                 # all models
    python benchmarks/stt_benchmark.py --models base_turbo kk_tulpar
    python benchmarks/stt_benchmark.py --device cpu    # force CPU

Output:
    benchmarks/results/stt_results_<timestamp>.csv  (per-file rows)
    summary table printed to stdout (mean WER/CER/time per model x language)
"""
import argparse
import csv
import platform
import re
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import jiwer

DATA_DIR = Path(__file__).parent / "data"
RESULTS_DIR = Path(__file__).parent / "results"
AUDIO_EXT = {".wav", ".mp3", ".ogg", ".m4a", ".webm"}
LANG_HINT = {"kk": "kk", "ru": "ru", "en": "en", "mixed": None}  # None = auto-detect


def pick_device(forced: str | None) -> str:
    if forced:
        return forced
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        return "cpu"


# ---------- models ----------

class FasterWhisper:
    """Base multilingual Whisper via faster-whisper (CTranslate2)."""

    def __init__(self, size: str, device: str):
        from faster_whisper import WhisperModel
        compute = "float16" if device == "cuda" else "int8"
        self.model = WhisperModel(size, device=device, compute_type=compute)

    def __call__(self, path: Path, lang: str | None) -> tuple[str, str]:
        segments, info = self.model.transcribe(str(path), language=lang, beam_size=5)
        return " ".join(s.text for s in segments).strip(), info.language


class HFWhisper:
    """Fine-tuned Whisper from Hugging Face (e.g. Kazakh KSC2 models)."""

    def __init__(self, model_id: str, device: str, force_lang: str | None = None):
        from transformers import pipeline
        self.force_lang = force_lang
        self.pipe = pipeline(
            "automatic-speech-recognition", model=model_id,
            device=0 if device == "cuda" else -1, chunk_length_s=30,
        )

    def __call__(self, path: Path, lang: str | None) -> tuple[str, str]:
        lang = self.force_lang or lang
        kwargs = {"generate_kwargs": {"language": lang, "task": "transcribe"}} if lang else {}
        return self.pipe(str(path), **kwargs)["text"].strip(), lang or "?"


class Routed:
    """Final pipeline: detect language with base model, send kk/mixed to the Kazakh model."""

    def __init__(self, base: FasterWhisper, kk: HFWhisper):
        self.base, self.kk = base, kk

    def __call__(self, path: Path, lang: str | None) -> tuple[str, str]:
        if lang is None:  # mixed / unknown: detect, restricted to kk/ru/en
            _, info = self.base.model.transcribe(str(path), beam_size=1)
            probs = dict(info.all_language_probs or [])
            lang = max(("kk", "ru", "en"), key=lambda l: probs.get(l, 0.0))
        if lang == "kk":
            return self.kk(path, "kk")
        return self.base(path, lang)


MODEL_FACTORIES = {
    "base_turbo": lambda d: FasterWhisper("large-v3-turbo", d),
    "kk_tulpar": lambda d: HFWhisper("olzhasAl/whisper-large-v3-tulpar", d, force_lang="kazakh"),
    "kk_turbo_ksc2": lambda d: HFWhisper("abilmansplus/whisper-turbo-ksc2", d, force_lang="kazakh"),
    "kk_base_small": lambda d: HFWhisper("akuzdeuov/whisper-base.kk", d),
}


# ---------- metrics ----------

def normalize(text: str) -> str:
    text = text.lower().replace("ё", "е")
    text = re.sub(r"[^\w\s]", " ", text)  # drop punctuation, keep Cyrillic/Latin letters
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=list(MODEL_FACTORIES) + ["routed"],
                    help=f"subset of {list(MODEL_FACTORIES) + ['routed']}")
    ap.add_argument("--device", choices=["cpu", "cuda"])
    ap.add_argument("--routed-kk", default="kk_tulpar", help="Kazakh model used by 'routed'")
    args = ap.parse_args()

    device = pick_device(args.device)
    hw = f"{platform.processor() or platform.machine()} / {device}"
    print(f"Device: {hw}")

    samples = sorted(p for p in DATA_DIR.rglob("*") if p.suffix.lower() in AUDIO_EXT)
    samples = [p for p in samples if p.with_suffix(".txt").exists()]
    if not samples:
        raise SystemExit(f"No audio with reference .txt found in {DATA_DIR}")

    loaded: dict[str, object] = {}

    def get(name: str):
        if name not in loaded:
            print(f"Loading {name} ...")
            if name == "routed":
                loaded[name] = Routed(get("base_turbo"), get(args.routed_kk))
            else:
                loaded[name] = MODEL_FACTORIES[name](device)
        return loaded[name]

    rows = []
    for name in args.models:
        model = get(name)
        for audio in samples:
            lang = audio.parent.name
            reference = normalize(audio.with_suffix(".txt").read_text(encoding="utf-8"))
            start = time.perf_counter()
            try:
                hyp, detected = model(audio, LANG_HINT.get(lang))
                error = ""
            except Exception as e:  # keep going if one model fails on a file
                hyp, detected, error = "", "", str(e)[:200]
            elapsed = time.perf_counter() - start
            hyp_n = normalize(hyp)
            wer = jiwer.wer(reference, hyp_n) if hyp_n else 1.0
            cer = jiwer.cer(reference, hyp_n) if hyp_n else 1.0
            rows.append({
                "model": name, "lang": lang, "detected_lang": detected, "file": audio.name,
                "wer": round(wer, 4), "cer": round(cer, 4), "time_s": round(elapsed, 2),
                "device": device, "hypothesis": hyp, "error": error,
            })
            print(f"{name:14} {lang:6} {audio.name:25} WER={wer:.3f} CER={cer:.3f} {elapsed:.1f}s")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULTS_DIR / f"stt_results_{datetime.now():%Y%m%d_%H%M%S}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    agg = defaultdict(list)
    for r in rows:
        agg[(r["model"], r["lang"])].append(r)
    print(f"\nHardware: {hw}")
    print("model          lang    n  WER    CER    time")
    for (m, lang), rs in sorted(agg.items()):
        n = len(rs)
        print(f"{m:14} {lang:6} {n:2}  "
              f"{sum(r['wer'] for r in rs)/n:.3f}  {sum(r['cer'] for r in rs)/n:.3f}  "
              f"{sum(r['time_s'] for r in rs)/n:.1f}s")
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
