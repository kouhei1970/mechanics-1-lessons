#!/usr/bin/env python3
"""TTS 読み辞書（lesson11 固有）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
長い複合語から先に置換する。共通DB（reference/tts_readings.json）に無い語のみここに置く。

TTS dictionary for lesson11. Readings in katakana only (hiragana は/へ become
particles ワ/エ). Replace longest terms first. Only terms absent from the common DB."""
REPLACEMENTS = [
    # 初速度: pyopenjtalk が「ハツソクド」と誤読するため「ショソクド」に固定
    # 初速度 (initial velocity) is misread as ハツソクド; fix to ショソクド
    ("初速度", "ショソクド"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
