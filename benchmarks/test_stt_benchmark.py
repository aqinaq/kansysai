"""Unit tests for the routing policy and evaluation modes of stt_benchmark.py.

They use stub models, so no model weights or GPU are needed:
    python -m pytest benchmarks/test_stt_benchmark.py -q
"""
from pathlib import Path

import pytest

import stt_benchmark as sb


class StubBase(sb.FasterWhisper):
    """FasterWhisper without loading a model: returns fixed language probabilities."""

    def __init__(self, probs):
        self.probs = probs
        self.decoded_with = []

    def language_probs(self, path):
        return self.probs

    def decode(self, path, lang):
        self.decoded_with.append(lang)
        return f"base:{lang}"


class StubKK(sb.HFWhisperKK):
    def __init__(self):
        self.name = "kk_stub"
        self.calls = 0

    def decode(self, path):
        self.calls += 1
        return "kk"


AUDIO = Path("x.wav")


# ---------- choose_route ----------

@pytest.mark.parametrize("probs, expected", [
    ({"kk": 0.7, "ru": 0.2, "en": 0.1}, ("kk", "kk")),            # clearly Kazakh
    ({"ru": 0.9, "en": 0.05, "kk": 0.05}, ("ru", "base")),         # clearly Russian
    ({"en": 0.95, "ru": 0.03, "kk": 0.02}, ("en", "base")),        # clearly English
    ({"ru": 0.55, "kk": 0.35, "en": 0.10}, ("ru", "kk")),          # mixed kk+ru: kk above threshold
    ({"tr": 0.6, "kk": 0.2, "ru": 0.2}, ("kk", "kk")),             # Turkish ignored, renormalised
    ({"tr": 1.0}, ("kk", "kk")),                                   # no kk/ru/en: default Kazakh
])
def test_choose_route(probs, expected):
    assert sb.choose_route(probs) == expected


def test_threshold_is_configurable():
    probs = {"ru": 0.6, "kk": 0.35, "en": 0.05}
    assert sb.choose_route(probs, kk_threshold=0.30)[1] == "kk"
    assert sb.choose_route(probs, kk_threshold=0.50)[1] == "base"


# ---------- hints ----------

def test_hint_for_mixed_is_kazakh():
    assert [sb.hint_for(f) for f in sb.FOLDERS] == ["kk", "ru", "en", "kk"]


# ---------- routed pipeline ----------

def test_routed_mixed_auto_goes_to_kazakh_model():
    base, kk = StubBase({"ru": 0.55, "kk": 0.35, "en": 0.10}), StubKK()
    res = sb.Routed(base, kk).transcribe(AUDIO, None, sb.KK_THRESHOLD)
    assert (res.routed_to, res.language, res.detected) == ("kk_stub", "kk", "ru")
    assert base.decoded_with == []


def test_routed_russian_auto_goes_to_base_with_detected_language():
    base, kk = StubBase({"ru": 0.9, "kk": 0.05, "en": 0.05}), StubKK()
    res = sb.Routed(base, kk).transcribe(AUDIO, None, sb.KK_THRESHOLD)
    assert (res.routed_to, res.language, res.detected) == ("base_turbo", "ru", "ru")
    assert kk.calls == 0


def test_routed_hint_skips_detection():
    # probabilities say Russian, but the user selected Kazakh: hint wins, nothing is detected
    base, kk = StubBase({"ru": 0.99, "kk": 0.0, "en": 0.01}), StubKK()
    res = sb.Routed(base, kk).transcribe(AUDIO, "kk", sb.KK_THRESHOLD)
    assert (res.routed_to, res.language, res.detected) == ("kk_stub", "kk", "")


def test_routed_english_hint_uses_base():
    base, kk = StubBase({"kk": 0.9}), StubKK()
    res = sb.Routed(base, kk).transcribe(AUDIO, "en", sb.KK_THRESHOLD)
    assert (res.routed_to, res.language) == ("base_turbo", "en")
    assert base.decoded_with == ["en"]


# ---------- base model ----------

def test_base_auto_detects_among_three_languages_only():
    base = StubBase({"tr": 0.7, "kk": 0.2, "ru": 0.1})
    res = base.transcribe(AUDIO, None, sb.KK_THRESHOLD)
    assert (res.language, res.detected) == ("kk", "kk")


def test_base_hint_is_not_reported_as_detection():
    res = StubBase({"ru": 1.0}).transcribe(AUDIO, "en", sb.KK_THRESHOLD)
    assert (res.language, res.detected) == ("en", "")


# ---------- modes ----------

def test_modes_for_models():
    assert sb.modes_for(StubBase({}), ["auto", "hint"]) == ["auto", "hint"]
    assert sb.modes_for(StubBase({}), ["auto"]) == ["auto"]
    assert sb.modes_for(StubKK(), ["auto", "hint"]) == ["forced_kk"]
