#!/usr/bin/env python3
"""
vibe-validate — quality gate for the vibe-translator skill.

Checks whether an adapted piece of content actually got REBUILT for its
target context, or whether it's secretly a literal translation wearing a
costume. Heuristic, not gospel — it flags smells for Claude to address,
it does not auto-grade.

Usage:
    python validate.py --target xhs --source source.txt --adapted adapted.txt
    python validate.py --target linkedin --adapted adapted.txt

Targets: xhs (小红书) | weibo | linkedin | twitter | jp_formal | jp_casual
"""

import argparse
import re
import sys

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F02F]"
)
HASHTAG_RE = re.compile(r"#\S+")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
KANA_RE = re.compile(r"[\u3040-\u30ff]")
LATIN_RE = re.compile(r"[A-Za-z]{3,}")


def lines(text):
    return [l for l in text.splitlines() if l.strip()]


def emoji_count(text):
    return len(EMOJI_RE.findall(text))


def structural_parallelism(source, adapted):
    """If adapted has ~same line count as source, it smells like a 1:1 port."""
    s, a = len(lines(source)), len(lines(adapted))
    if s == 0:
        return None
    ratio = a / s
    return ratio


def check(target, source, adapted):
    flags = []
    passes = []
    n_lines = len(lines(adapted))
    n_emoji = emoji_count(adapted)
    n_hash = len(HASHTAG_RE.findall(adapted))
    has_cjk = bool(CJK_RE.search(adapted))
    has_kana = bool(KANA_RE.search(adapted))
    has_latin = bool(LATIN_RE.search(adapted))

    # --- language sanity ---
    if target in ("xhs", "weibo") and not has_cjk:
        flags.append("Target is a Chinese platform but no Chinese characters found.")
    if target in ("jp_formal", "jp_casual") and not (has_kana or has_cjk):
        flags.append("Target is Japanese but no kana/kanji found.")
    if target in ("linkedin", "twitter") and has_cjk and has_latin:
        # mixed is fine, but heavy CJK on an English target is a smell
        cjk_n = len(CJK_RE.findall(adapted))
        if cjk_n > 10:
            flags.append("Heavy CJK on an English-target post — was this actually adapted?")

    # --- platform convention checks ---
    if target == "xhs":
        if n_emoji < 2:
            flags.append("XHS post with <2 emoji — XHS rewards expressive emoji use.")
        else:
            passes.append(f"Emoji present ({n_emoji}) — good for XHS.")
        if n_hash < 2:
            flags.append("XHS post with <2 hashtags — add a topic cluster (#话题).")
        else:
            passes.append(f"Hashtag cluster present ({n_hash}).")
        if n_lines < 3:
            flags.append("Very few line breaks — XHS favours short, scannable lines.")

    elif target == "twitter":
        chars = len(adapted)
        if chars > 280 and "\n\n" not in adapted:
            flags.append(f"{chars} chars with no thread breaks — tighten or split into a thread.")
        else:
            passes.append("Length/structure reasonable for X.")
        if n_hash > 3:
            flags.append("Many hashtags — X rewards restraint (0–2 is native).")

    elif target == "linkedin":
        if n_lines < 3:
            flags.append("Dense block — LinkedIn favours line breaks between sentences.")
        else:
            passes.append("Good line-break spacing for LinkedIn readability.")
        if n_emoji > 8:
            flags.append("Heavy emoji for LinkedIn — dial back to a few.")

    elif target == "jp_formal":
        # crude keigo / humility signal
        humility = any(k in adapted for k in ["恐縮", "おかげさま", "させていただ", "存じ", "幸い"])
        if not humility:
            flags.append("No humility/keigo markers detected — formal JP usually softens self-reference.")
        else:
            passes.append("Humility/keigo markers present.")
        if n_emoji > 2:
            flags.append("Emoji-heavy for formal Japanese context.")

    # --- the big one: literal-translation smell ---
    if source:
        ratio = structural_parallelism(source, adapted)
        if ratio is not None and 0.85 <= ratio <= 1.15:
            flags.append(
                f"Adapted line count ({len(lines(adapted))}) ≈ source "
                f"({len(lines(source))}) — possible 1:1 port. A real rebuild "
                f"usually restructures."
            )
        elif ratio is not None:
            passes.append("Structure diverges from source — looks rebuilt, not ported.")

    return flags, passes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True,
                    choices=["xhs", "weibo", "linkedin", "twitter",
                             "jp_formal", "jp_casual"])
    ap.add_argument("--source")
    ap.add_argument("--adapted", required=True)
    args = ap.parse_args()

    def load(p):
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()

    source = load(args.source) if args.source else ""
    adapted = load(args.adapted)

    flags, passes = check(args.target, source, adapted)

    print("=" * 56)
    print(f"VIBE VALIDATE — target: {args.target}")
    print("=" * 56)

    if passes:
        print("\n✓ LOOKS RIGHT")
        for p in passes:
            print(f"  ✓ {p}")

    if flags:
        print("\n⚠ SMELLS TO ADDRESS")
        for fl in flags:
            print(f"  ⚠ {fl}")
    else:
        print("\nNo smells detected. Still gut-check: would a native post this?")

    print("\n" + "=" * 56)
    print("Heuristic only. The native-fluency test is human + Claude's call.")
    print("=" * 56)
    sys.exit(1 if flags else 0)


if __name__ == "__main__":
    main()
