#!/usr/bin/env python3
"""TTS 読み辞書（lesson10 固有・最小）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
長い複合語から先に置換。共通DB reference/tts_readings.json に無い語・助詞補正のみここに置く。"""
REPLACEMENTS = [
    # 反力は共通DBにも追加済みだが、本レッスン単独で再生できるよう保険として残す
    # 反力 reading kept here so this lesson can regenerate audio standalone (×ハンチカラ)
    ("反力", "ハンリョク"),
]
def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
