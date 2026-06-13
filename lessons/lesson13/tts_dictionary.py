#!/usr/bin/env python3
"""TTS 読み辞書（lesson13 固有）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
長い複合語から先に置換する。共通DB（reference/tts_readings.json）に無い語のみここに置く。

TTS dictionary for lesson13. Readings in katakana only (hiragana は/へ become
particles ワ/エ). Replace longest terms first. Only terms absent from the common DB."""
REPLACEMENTS = [
    # 向心: pyopenjtalk が「向心加速度」を「コーココロ…」「ムカイココロ」と誤読するため固定
    # 向心 is misread (コーココロ/ムカイココロ); fix the compounds to コーシン
    ("向心加速度", "コーシンカソクド"),
    ("向心力", "コーシンリョク"),
    ("向心", "コーシン"),
    # 船速: 「フネソク」と誤読されるため「センソク」に固定
    # 船速 (boat speed) is misread as フネソク; fix to センソク
    ("船速", "センソク"),
    # 序数「一つめ／二つめ／三つめ」が イチツメ／ニツメ／ミツメ と誤読されるため固定
    # ordinals 一つめ/二つめ/三つめ are misread; fix to ヒトツメ/フタツメ/ミッツメ
    ("一つめ", "ヒトツメ"),
    ("二つめ", "フタツメ"),
    ("三つめ", "ミッツメ"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
