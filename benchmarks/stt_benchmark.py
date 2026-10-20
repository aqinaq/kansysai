"""
STT benchmark for BE-03 (DEMO-22): compares LOCAL speech-to-text models on kk/ru/en/mixed audio.

Folder layout:
    benchmarks/data/<lang>/<name>.<wav|mp3|ogg|m4a|webm>   # lang: kk, ru, en, mixed
    benchmarks/data/<lang>/<name>.txt                       # reference transcript

Evaluation modes
----------------
Every multilingual model is evaluated in two modes, reported separately:

auto  - no language information is given. The language is detected automatically,
        restricted to kk/ru/en (as in the product pipeline). This is the default
        product behaviour and the main result.
hint  - the user has selected the language in the UI. The hint is the folder language
        for kk/ru/en; for mixed recordings the hint is "kk", because the UI offers
        Kazakh for mixed Kazakh-Russian-English speech.

Kazakh-only fine-tuned models (kk_*) always decode in Kazakh, so they are run once
in mode "forced_kk".

Routing policy (same as BE-03, section "Speech-to-Text")
--------------------------------------------------------
  * with a hint:  kk -> Kazakh model, ru/en -> base Whisper
  * without hint: language probabilities are restricted to kk/ru/en and renormalised;
                the Kazakh model is used if kk is the most likely language OR
                p(kk) >= KK_THRESHOLD (default 0.30). Otherwise base Whisper is used
                with the detected language (ru or en).
The threshold sends mixed speech that is only partly Kazakh to the Kazakh model.

Usage:
    pip install faster-whisper transformers torch librosa jiwer
    python benchmarks/stt_benchmark.py                          # all models, both modes
    python benchmarks/stt_benchmark.py --models base_turbo routed --modes auto
    python benchmarks/stt_benchmark.py --device cpu --kk-threshold 0.3

Output:
    benchmarks/results/stt_results_<timestamp>.csv   per-file rows
    summary tables printed to stdout:
    - mean WER / CER / time per model x mode x language
    - language-detection accuracy (auto mode, kk/ru/en files)
    - routing decisions of the routed pipeline on mixed files
"""
import argparse
import csv
import platform
import re
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
RESULTS_DIR = Path(__file__).parent / "results"
AUDIO_EXT = {".wav", ".mp3", ".ogg", ".m4a", ".webm"}
LANGS = ("kk", "ru", "en")
FOLDERS = ("kk", "ru", "en", "mixed")
KK_THRESHOLD = 0.30


@dataclass
class STTResult:
    text: str
    language: str      # language used for decoding
    detected: str      # automatically detected language ("" if a hint/forced language was used)
    routed_to: str     # model that produced the text


def hint_for(folder: str) -> str:
    """Language the user would select in the UI for a recording from this folder."""
    return "kk" if folder == "mixed" else folder


def choose_route(probs: dict[str, float], kk_threshold: float = KK_THRESHOLD) -> tuple[str, str]:
    """Routing policy for automatic detection.

    probs: language probabilities from Whisper (any languages).
    Returns (detected_language, route) where route is "kk" or "base".
    """
    restricted = {lang: probs.get(lang, 0.0) for lang in LANGS}
    total = sum(restricted.values())
    if total <= 0:
        return "kk", "kk"  # nothing usable detected: default to the Kazakh model, as for mixed speech
    restricted = {lang: p / total for lang, p in restricted.items()}
    detected = max(restricted, key=restricted.get)
    if detected == "kk" or restricted["kk"] >= kk_threshold:
        return detected, "kk"
    return detected, "base"


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
    name = "base_turbo"
    multilingual = True

    def __init__(self, size: str, device: str):
        from faster_whisper import WhisperModel
        compute = "float16" if device == "cuda" else "int8"
        self.model = WhisperModel(size, device=device, compute_type=compute)

    def language_probs(self, path: Path) -> dict[str, float]:
        # transcribe() returns a lazy generator; info is available without decoding segments
        _, info = self.model.transcribe(str(path), beam_size=1)
        return dict(info.all_language_probs or [])

    def decode(self, path: Path, lang: str) -> str:
        segments, _ = self.model.transcribe(str(path), language=lang, beam_size=5)
        return " ".join(s.text for s in segments).strip()

    def transcribe(self, path: Path, hint: str | None, kk_threshold: float) -> STTResult:
        if hint:
            return STTResult(self.decode(path, hint), hint, "", self.name)
        detected, _ = choose_route(self.language_probs(path), kk_threshold)
        return STTResult(self.decode(path, detected), detected, detected, self.name)


class HFWhisperKK:
    """Kazakh-only fine-tuned Whisper from Hugging Face (KSC2 models). Always decodes Kazakh."""
    multilingual = False

    def __init__(self, name: str, model_id: str, device: str):
        from transformers import pipeline
        self.name = name
        self.pipe = pipeline(
            "automatic-speech-recognition", model=model_id,
            device=0 if device == "cuda" else -1, chunk_length_s=30,
        )

    def decode(self, path: Path) -> str:
        out = self.pipe(str(path), generate_kwargs={"language": "kazakh", "task": "transcribe"})
        return out["text"].strip()

    def transcribe(self, path: Path, hint: str | None, kk_threshold: float) -> STTResult:
        return STTResult(self.decode(path), "kk", "", self.name)


class Routed:
    """Product pipeline: base Whisper for ru/en, Kazakh model for kk and mixed speech."""
    name = "routed"
    multilingual = True

    def __init__(self, base: FasterWhisper, kk: HFWhisperKK):
        self.base, self.kk = base, kk

    def transcribe(self, path: Path, hint: str | None, kk_threshold: float) -> STTResult:
        if hint:
            detected, route = "", ("kk" if hint == "kk" else "base")
            lang = hint
        else:
            detected, route = choose_route(self.base.language_probs(path), kk_threshold)
            lang = "kk" if route == "kk" else detected
        if route == "kk":
            return STTResult(self.kk.decode(path), "kk", detected, self.kk.name)
        return STTResult(self.base.decode(path, lang), lang, detected, self.base.name)


KK_MODELS = {
    "kk_tulpar": "olzhasAl/whisper-large-v3-tulpar",
    "kk_turbo_ksc2": "abilmansplus/whisper-turbo-ksc2",
    "kk_base_small": "akuzdeuov/whisper-base.kk",
}
ALL_MODELS = ["base_turbo", *KK_MODELS, "routed"]


# ---------- metrics ----------

def normalize(text: str) -> str:
    text = text.lower().replace("ё", "е")
    text = re.sub(r"[^\w\s]", " ", text)  # drop punctuation, keep Cyrillic/Latin letters
    return re.sub(r"\s+", " ", text).strip()


def modes_for(model, requested: list[str]) -> list[str]:
    return [m for m in requested if m in ("auto", "hint")] if model.multilingual else ["forced_kk"]


def summarize(rows: list[dict]) -> None:
    agg = defaultdict(list)
    for r in rows:
        agg[(r["model"], r["mode"], r["lang"])].append(r)
    print("\nWER / CER / time per model x mode x language")
    print(f"{'model':14} {'mode':10} {'lang':6} {'n':>3}  {'WER':>6} {'CER':>6} {'time':>6}")
    for (m, mode, lang), rs in sorted(agg.items()):
        n = len(rs)
        print(f"{m:14} {mode:10} {lang:6} {n:3}  "
            f"{sum(r['wer'] for r in rs)/n:6.3f} {sum(r['cer'] for r in rs)/n:6.3f} "
            f"{sum(r['time_s'] for r in rs)/n:5.1f}s")

    det = defaultdict(lambda: [0, 0])
    for r in rows:
        if r["mode"] == "auto" and r["lang"] in LANGS and r["detected_lang"]:
            key = (r["model"], r["lang"])
            det[key][0] += r["detected_lang"] == r["lang"]
            det[key][1] += 1
    if det:
        print("\nLanguage detection accuracy (auto mode, kk/ru/en files)")
        for (m, lang), (ok, n) in sorted(det.items()):
            print(f"{m:14} {lang:6} {ok}/{n}")

    routes = defaultdict(int)
    for r in rows:
        if r["model"] == "routed" and r["mode"] == "auto" and r["lang"] == "mixed":
            routes[r["routed_to"]] += 1
    if routes:
        print("\nRouting of mixed recordings (routed, auto mode)")
        for target, n in sorted(routes.items()):
            print(f"  -> {target}: {n}")


def main() -> None:
    import jiwer

    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=ALL_MODELS, choices=ALL_MODELS)
    ap.add_argument("--modes", nargs="+", default=["auto", "hint"], choices=["auto", "hint"],
                    help="modes for multilingual models; kk_* models always run as forced_kk")
    ap.add_argument("--device", choices=["cpu", "cuda"])
    ap.add_argument("--routed-kk", default="kk_tulpar", choices=list(KK_MODELS),
                    help="Kazakh model used by the routed pipeline")
    ap.add_argument("--kk-threshold", type=float, default=KK_THRESHOLD,
                    help="p(kk) above which auto mode routes to the Kazakh model")
    args = ap.parse_args()

    device = pick_device(args.device)
    hw = f"{platform.processor() or platform.machine()} / {device}"
    print(f"Device: {hw}  |  kk threshold: {args.kk_threshold}")

    samples = sorted(p for p in DATA_DIR.rglob("*")
                    if p.suffix.lower() in AUDIO_EXT and p.parent.name in FOLDERS)
    samples = [p for p in samples if p.with_suffix(".txt").exists()]
    if not samples:
        raise SystemExit(f"No audio with reference .txt found in {DATA_DIR}/<kk|ru|en|mixed>/")

    loaded: dict[str, object] = {}

    def get(name: str):
        if name not in loaded:
            print(f"Loading {name} ...")
            if name == "base_turbo":
                loaded[name] = FasterWhisper("large-v3-turbo", device)
            elif name == "routed":
                loaded[name] = Routed(get("base_turbo"), get(args.routed_kk))
            else:
                loaded[name] = HFWhisperKK(name, KK_MODELS[name], device)
        return loaded[name]

    rows = []
    for name in args.models:
        model = get(name)
        for mode in modes_for(model, args.modes):
            for audio in samples:
                folder = audio.parent.name
                hint = hint_for(folder) if mode == "hint" else None
                reference = normalize(audio.with_suffix(".txt").read_text(encoding="utf-8"))
                start = time.perf_counter()
                try:
                    res = model.transcribe(audio, hint, args.kk_threshold)
                    error = ""
                except Exception as e:  # keep going if one model fails on a file
                    res, error = STTResult("", "", "", ""), str(e)[:200]
                elapsed = time.perf_counter() - start
                hyp = normalize(res.text)
                wer = jiwer.wer(reference, hyp) if hyp else 1.0
                cer = jiwer.cer(reference, hyp) if hyp else 1.0
                rows.append({
                    "model": name, "mode": mode, "lang": folder, "hint": hint or "",
                    "detected_lang": res.detected, "decode_lang": res.language,
                    "routed_to": res.routed_to, "file": audio.name,
                    "wer": round(wer, 4), "cer": round(cer, 4), "time_s": round(elapsed, 2),
                    "device": device, "kk_threshold": args.kk_threshold,
                    "hypothesis": res.text, "error": error,
                })
                print(f"{name:14} {mode:10} {folder:6} {audio.name:25} "
                      f"det={res.detected or '-':3} -> {res.routed_to or '-':14} "
                      f"WER={wer:.3f} CER={cer:.3f} {elapsed:.1f}s")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULTS_DIR / f"stt_results_{datetime.now():%Y%m%d_%H%M%S}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nHardware: {hw}")
    summarize(rows)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
