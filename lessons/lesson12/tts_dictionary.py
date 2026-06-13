#!/usr/bin/env python3
"""TTS 読み辞書（lesson12）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
共通DB reference/tts_readings.json が放物運動・接線/法線加速度などの語をカバーするため、
lesson 固有の追加は不要（空）。誤読が見つかれば長い複合語から先にカタカナで追加。"""
REPLACEMENTS = [
]
def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
