# 🌐 vibe-translator

> A Claude skill that adapts content across **any language, culture, and platform** — without it sounding translated.

Google Translate moves *words* between languages. `vibe-translator` does the harder thing: it carries content **across cultures and platforms** and rebuilds it so a native of the destination would never guess it started somewhere else.

The gap that matters isn't vocabulary — it's *culture*: directness vs. indirectness, self-promotion norms, individual vs. collective framing, humor that doesn't survive a literal hop, formality register, emoji and formatting conventions, and the unspoken "would a local actually post this?" test. Works in **any direction, any language pair**.

---

## See it work

**Input** — an English Twitter/X hot take:

> "Hot take: everyone's obsessed with NVIDIA but the real AI trade is power & cooling. You can't run a GPU you can't cool. Networking, energy, thermal — that's where the next 10x is hiding."

**Output** — rebuilt for Xiaohongshu (小红书):

> 🔥 说个有点反共识的观点:大家都在盯着英伟达,但AI真正的机会其实在「电力」和「散热」👀
>
> 逻辑很简单——GPU再强,散不了热也跑不起来⚡️
>
> 网络、能源、散热… 这些「卖铲子」的环节才是下一个10倍藏的地方💰
>
> 姐妹们怎么看?评论区聊聊～👇
>
> #AI投资 #英伟达 #美股 #投资笔记

It didn't translate the words. It changed structure, pacing, emoji norms, and added the community hook XHS posts live on — because that's what a native would do. The same method works for **any** target: English → Spanish Instagram, Japanese → Western LinkedIn, Chinese → English Reddit.

---

## What it handles

**Languages & cultures:** any, in any direction — the cultural-adaptation method is universal.

**Platform registers (examples, not a limit):** LinkedIn · Xiaohongshu (小红书) · Weibo · Twitter/X · Instagram · TikTok · Reddit · formal/business registers · marketing copy · emails

---

## Quality gate (bundled)

Ships with `scripts/validate.py` — a heuristic checker for the most common targets (`xhs` · `weibo` · `linkedin` · `twitter` · `jp_formal` · `jp_casual`) that catches "this is secretly a literal translation" smells before you post: missing platform markers, wrong-language output, and structure that mirrors the source 1:1.

```bash
python scripts/validate.py --target xhs --source source.txt --adapted adapted.txt
```

Pure Python 3, no dependencies. For languages/platforms it doesn't cover, the native-fluency call stays yours.

---

## How to use it

Once installed, just ask Claude naturally:

- *"Post this on Xiaohongshu"*
- *"Make this sound natural in Korean"*
- *"Rewrite this English launch post for Spanish Instagram"*
- *"Adapt this announcement for my Japanese audience"*

The skill loads automatically when the destination has different cultural conventions than the source.

---

## Install

### Drop-in
```
your-skills-directory/
└── vibe-translator/
    ├── SKILL.md
    └── scripts/
```

### Claude Code
```bash
git clone https://github.com/3243dwon/vibe-translator.git
cp -r vibe-translator ~/.claude/skills/
```

Works across **Claude.ai, Claude Code, and the Claude API**; the `SKILL.md` format is portable to other agents (Cursor, Codex, Gemini CLI).

---

## License

MIT — use it, fork it, build on it.
