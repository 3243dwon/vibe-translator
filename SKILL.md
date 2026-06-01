---
name: vibe-translator
description: Bridge content across the English, Chinese, and Japanese cultural spheres so it lands authentically with a native audience — not a word-for-word translation, but a rebuild that respects tone, conventions, and unspoken cultural rules. Unlike single-market localizers, this skill works trilingually and bidirectionally (EN ↔ ZH ↔ JP), and is fluent in the cultural register of each platform within those spheres (LinkedIn, Xiaohongshu/小红书, Weibo, Twitter/X, Instagram, Japanese formal/business). Use whenever someone wants to move content across these cultures, across platforms, or both. Trigger on phrases like "make this work for [platform]", "post this on Xiaohongshu", "rewrite this for a Chinese/Japanese audience", "localize this", "make this sound natural in [language]", "adapt this for [culture]", or any request where a direct translation would feel off, stiff, or foreign. Use even when the user only says "translate" but the destination has different cultural conventions than the source.
---

# Vibe Translator

Most translation moves *words* from one language to another. This skill moves *vibe* — the cultural and platform context that makes content actually land.

A perfectly accurate translation of a LinkedIn post into Chinese will read as a translated LinkedIn post. It will feel foreign on Xiaohongshu, where the native conventions are completely different. The job here is not translation. It is **rebuilding the content as if a native of the target context had written it from scratch.**

**What makes this different from single-market content tools:** most localizers operate inside *one* culture (e.g. Chinese platform → Chinese platform). This skill bridges *across* the three big cultural spheres — Western, Chinese, and Japanese — in any direction. The hardest and most valuable cases are cross-cultural: an English founder's announcement that needs to land on 小红书, a Japanese product update that needs Western directness, a Chinese investing take rebuilt for an English audience. That cross-cultural bridge is the core competency here.

## Core principle

> Don't ask "what do these words mean in the other language?"
> Ask "how would a native of the target context express this same intent?"

This often means changing structure, length, tone, emoji usage, formatting, references, and level of directness — not just vocabulary.

## Required inputs

Before adapting, establish (ask only if genuinely unclear):

1. **The content** — what's being adapted
2. **Source context** — origin language + platform/setting (e.g. English LinkedIn)
3. **Target context** — destination language + platform/setting (e.g. Chinese Xiaohongshu)
4. **Intent** — what the content is trying to *achieve* (announce, persuade, sell, vent, connect, inform). This is what gets preserved; everything else can change.

If the user gives content but no target, infer the most likely one and state your assumption.

## The adaptation process

1. **Extract the intent.** Strip away the surface form. What is this content actually *doing*?
2. **Diagnose the source conventions.** Why does it work (or not) in its origin context?
3. **Load the target conventions.** What are the native rules of the destination? (See the cheat sheet below.)
4. **Rebuild from intent.** Write fresh content native to the target — don't translate the original sentence by sentence.
5. **Gut check.** Would a local actually post this? If it smells translated, redo it.

## Platform & culture cheat sheet

Use this as a reference, not a script. Real fluency means knowing when to break these.

### Xiaohongshu / 小红书 (Chinese)
- Warm, personal, peer-to-peer ("姐妹们", "宝子们", "家人们")
- Heavy emoji and emoji-as-punctuation; generous line breaks, short lines
- Aesthetic and lifestyle framing even for serious topics
- Hooks matter: first line must stop the scroll
- Hashtags clustered at the end (#话题)
- Flex culture exists but is softened with relatability ("普通女生也可以…")
- Avoids the stiff achievement-brag tone of LinkedIn

### Weibo (Chinese)
- More public-square, trend-aware, opinionated
- Punchier than XHS, more discourse-driven
- Topic tags #话题# bracket-style

### LinkedIn (English/Western)
- Achievement-oriented, "thrilled / excited / humbled to share"
- Narrative arc, often a personal-lesson framing
- Line breaks between most sentences for readability
- Professional but increasingly personal/storytelling
- Soft humble-brag is the native dialect

### Twitter / X (English)
- Punchy, opinionated, often lowercase for tone
- Hot takes, threads, no filler
- Hooks and brevity win; cut every spare word

### Japanese business / formal (Japanese)
- Indirect, group-oriented, modest about individual achievement
- Keigo (敬語) register; humility markers (恐縮ですが, おかげさまで)
- Conclusions softened; reading-the-air (空気を読む) matters
- Avoid blunt self-promotion that reads fine in English

### Japanese casual / social (Japanese)
- Lighter, emoji and kaomoji (笑), more playful
- Still less self-promotional than Western social norms

### Instagram (English/global)
- Visual-first; caption supports the image
- Casual, aspirational, emoji-friendly, hashtag clusters

## Cultural dimensions to watch

- **Directness:** US/UK direct → Japan highly indirect; China context-dependent
- **Self-promotion:** Acceptable and expected on LinkedIn; needs softening for Japanese formal contexts; reframed-as-relatable on XHS
- **Individual vs collective:** Western "I achieved" → often reframed toward group/gratitude in Japanese contexts
- **Humor:** Rarely translates literally — rebuild the joke for the target, or cut it
- **Formality register:** Match the destination, not the source

## Output format

Deliver:

1. **The adapted content** — ready to post, native to the target. This is the main deliverable; lead with it.

2. **Adaptation notes** — 2–4 bullets on the key decisions you made and why (e.g. "Dropped the 'humbled to share' framing — reads as awkward on XHS; opened with a relatable hook instead"). Keep this short.

If the target language isn't English, still write the adaptation notes in the language the user is conversing in.

## Optional: validate before delivering

This skill bundles a heuristic checker at `scripts/validate.py`. It does **not** grade fluency — it catches mechanical "this is secretly a literal translation" smells: missing platform markers (emoji/hashtags on XHS, line breaks on LinkedIn, keigo on formal JP), wrong-language output, and structure that mirrors the source 1:1 (a tell that nothing was actually rebuilt).

Run it when you want a second pass before handing content over:

```bash
python scripts/validate.py --target xhs --source source.txt --adapted adapted.txt
```

Targets: `xhs` · `weibo` · `linkedin` · `twitter` · `jp_formal` · `jp_casual`. The `--source` flag is optional but enables the 1:1-port check. Treat any flags it raises as prompts to revise, then re-run — but the final "would a native actually post this?" judgment is still yours.

## Worked example

**Input:** English LinkedIn post → Xiaohongshu (Chinese)
> "Thrilled to announce I've accepted a Product Manager role at ByteDance! Grateful to everyone who supported me on this journey. Onwards and upwards! 🚀"

**Bad output (translated, not adapted):**
> "很高兴地宣布我已经接受了字节跳动的产品经理职位！感谢一路上支持我的每一个人。继续向上！🚀"
*(Accurate, but reads as a translated LinkedIn post. Stiff. No one posts like this on XHS.)*

**Good output (rebuilt for XHS):**
> 啊啊啊我拿到字节的PM offer啦！！！😭🎉
>
> 还有点不敢相信… 从投简历到面试到现在，真的太多人帮过我了🥹
>
> 普通人也可以的，真的！如果有姐妹也在准备产品岗，评论区可以一起聊～
>
> \#字节跳动 #产品经理 #offer #求职日记

**Adaptation notes:**
- Swapped the formal "宣布" announcement frame for raw excitement — XHS rewards emotional, scroll-stopping openers
- Added relatability ("普通人也可以的") and a community hook (评论区一起聊) — core to how XHS posts build engagement
- Hashtag cluster at the end, XHS-style

## Anti-patterns to avoid

- Translating sentence-by-sentence and calling it localized
- Keeping the source platform's structure (e.g. LinkedIn line breaks on a Twitter post)
- Over-formalizing casual content or over-casualizing formal content
- Forcing the source's humor or idioms into the target
- Producing something technically correct that no native would actually post
