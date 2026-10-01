---
name: vibe-translator
description: Adapt content across languages, cultures, and platforms so it reads as if a native wrote it from scratch — not word-for-word translation but a rebuild respecting tone, conventions, formatting, humor, and unspoken rules. Any language, any platform, any direction (LinkedIn, 小红书, Weibo, X, Instagram, TikTok, Reddit, business register, marketing, email). Trigger on 'localize this', 'translate this', 'post this on [platform]', 'rewrite for a [culture] audience', 'make this sound native'. 中文：把内容跨语言、跨文化、跨平台改写，读起来像当地人从零写的——不是逐字翻译，而是尊重目标语境的语气、惯例、排版、幽默和潜规则重建。支持任意语言/平台/方向（小红书、微博、X、LinkedIn、IG、TikTok、商务、营销、邮件）。触发词：「改成适合小红书的」「发到 X 上」「本地化一下」「翻译这个」「听起来像母语」。
---

# Vibe Translator

Most translation moves *words* from one language to another. This skill moves *vibe* — the cultural and platform context that makes content actually land.

A perfectly accurate translation of a LinkedIn post into another language will still read as a *translated LinkedIn post*. It will feel foreign on the destination platform, where the native conventions are completely different. The job here is not translation. It is **rebuilding the content as if a native of the target context had written it from scratch.**

**This works for any language, any culture, any platform, in any direction.** The method is universal: the value is in carrying *intent* across a cultural and platform gap — directness vs. indirectness, self-promotion norms, individual vs. collective framing, humor that doesn't survive a literal hop, formality register, emoji and formatting conventions, and the unspoken "would a local actually post this?" test.

## Core principle

> Don't ask "what do these words mean in the other language?"
> Ask "how would a native of the target context express this same intent?"

This often means changing structure, length, tone, emoji usage, formatting, references, and level of directness — not just vocabulary.

## Required inputs

Before adapting, establish (ask only if genuinely unclear):

1. **The content** — what's being adapted
2. **Source context** — origin language + platform/setting (e.g. English LinkedIn)
3. **Target context** — destination language + platform/setting (e.g. Spanish Instagram, Korean formal, Chinese Xiaohongshu)
4. **Intent** — what the content is trying to *achieve* (announce, persuade, sell, vent, connect, inform). This is what gets preserved; everything else can change.

If the user gives content but no target, infer the most likely one and state your assumption.

## The adaptation process

1. **Extract the intent.** Strip away the surface form. What is this content actually *doing*?
2. **Diagnose the source conventions.** Why does it work (or not) in its origin context?
3. **Load the target conventions.** What are the native rules of the destination language/platform? (Use the cheat sheet below as a starting point; reason from first principles for anything not listed.)
4. **Rebuild from intent.** Write fresh content native to the target — don't translate the original sentence by sentence.
5. **Gut check.** Would a local actually post this? If it smells translated, redo it.

## Platform & culture cheat sheet

Examples, **not** an exhaustive list. The same method applies to any language or platform not shown here — reason from the cultural dimensions below.

### Xiaohongshu / 小红书 (Chinese)
- Warm, personal, peer-to-peer ("姐妹们", "宝子们", "家人们"); heavy emoji; short lines, generous breaks
- Aesthetic/lifestyle framing even for serious topics; first line must stop the scroll; hashtags clustered at the end

### Weibo (Chinese)
- More public-square, trend-aware, opinionated; punchier than XHS; topic tags #话题#

### LinkedIn (Western/global professional)
- Achievement-oriented ("thrilled / humbled to share"); narrative arc, personal-lesson framing; line breaks between sentences; soft humble-brag is native

### Twitter / X
- Punchy, opinionated, often lowercase for tone; hot takes and threads; cut every spare word; 0–2 hashtags

### Japanese formal / business
- Indirect, group-oriented, modest; keigo (敬語) + humility markers (恐縮ですが, おかげさまで); conclusions softened; reading-the-air (空気を読む)

### Instagram / TikTok (global)
- Visual-first; caption supports the media; casual, aspirational; emoji-friendly
- Instagram: **hard cap of 5 hashtags** per post/Reel (since Dec 2025, first-comment tags included) — pick 3–5 specific ones; links in captions aren't clickable ("link in bio")
- TikTok: a few relevant hashtags at the end; no hashtag wall

## Cultural dimensions to watch (universal — use for ANY language)

- **Directness:** US/UK direct → Japan/Korea highly indirect; many cultures context-dependent
- **Self-promotion:** expected on LinkedIn; softened in many East-Asian formal contexts; reframed-as-relatable on lifestyle platforms
- **Individual vs. collective:** "I achieved" often reframes toward group/gratitude in collectivist contexts
- **Humor:** rarely translates literally — rebuild the joke for the target, or cut it
- **Formality register:** match the destination, not the source
- **Formatting & emoji:** density and style vary wildly by platform and culture

## Output format

Deliver:

1. **The adapted content** — ready to post, native to the target. Lead with it.
2. **Adaptation notes** — 2–4 bullets on the key decisions and why (e.g. "Dropped the 'humbled to share' framing — reads as awkward here; opened with a relatable hook instead"). Keep it short.

If the target language isn't English, still write the adaptation notes in the language the user is conversing in.

## Optional: validate before delivering

This skill bundles a heuristic checker at `scripts/validate.py` for the most common targets (`xhs`, `weibo`, `linkedin`, `twitter`, `jp_formal`, `jp_casual`). It catches mechanical "this is secretly a literal translation" smells — missing platform markers, wrong-language output, and structure that mirrors the source 1:1.

```bash
python scripts/validate.py --target xhs --source source.txt --adapted adapted.txt
```

For any language/platform the checker doesn't cover, skip it and rely on the native-fluency gut check — that judgment is always yours.

## Worked example

**Input:** English LinkedIn post → Xiaohongshu (Chinese)
> "Thrilled to announce I've accepted a Product Manager role at ByteDance! Grateful to everyone who supported me. Onwards and upwards! 🚀"

**Bad output (translated, not adapted):**
> "很高兴地宣布我已经接受了字节跳动的产品经理职位！感谢一路上支持我的每一个人。继续向上！🚀"
*(Accurate, but reads as a translated LinkedIn post. No one posts like this on XHS.)*

**Good output (rebuilt for XHS):**
> 啊啊啊我拿到字节的PM offer啦！！！😭🎉
>
> 还有点不敢相信… 从投简历到面试,真的太多人帮过我了🥹
>
> 普通人也可以的,真的!如果有姐妹也在准备产品岗,评论区一起聊～
>
> \#字节跳动 #产品经理 #offer #求职日记

**Adaptation notes:**
- Swapped the formal announcement frame for raw excitement — XHS rewards emotional, scroll-stopping openers
- Added relatability + a community hook — core to how XHS posts build engagement
- Hashtag cluster at the end, XHS-style

The same approach works in any direction and any language pair — e.g. a Japanese product update rebuilt with Western directness, a Chinese investing take rebuilt for an English audience, or an English launch post rebuilt for Spanish Instagram.

## Anti-patterns to avoid

- Translating sentence-by-sentence and calling it localized
- Keeping the source platform's structure (e.g. LinkedIn line breaks on a Twitter post)
- Over-formalizing casual content or over-casualizing formal content
- Forcing the source's humor or idioms into the target
- Producing something technically correct that no native would actually post
