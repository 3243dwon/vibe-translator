# 🌐 vibe-translator

> A Claude skill that bridges content across the **English, Chinese, and Japanese** cultural spheres — without it sounding translated.

Google Translate moves *words* between languages. Single-market content tools rewrite *within* one culture. `vibe-translator` does the hard thing neither does: it carries content **across** the three big cultural spheres — Western, Chinese, Japanese — and rebuilds it so a native of the destination would never guess it started somewhere else.

The hardest, most valuable cases are cross-cultural: an English founder's announcement that needs to land on 小红书, a Japanese product update that needs Western directness, a Chinese investing take rebuilt for an English audience. **That cross-cultural bridge is the whole point.**

---

## Why this isn't another localizer

Most platform-content skills operate inside a single language — Chinese platform → Chinese platform. `vibe-translator` is built for the **trilingual, bidirectional** problem (EN ↔ ZH ↔ JP), where the gap isn't vocabulary, it's *culture*: directness vs. indirectness, self-promotion norms, individual vs. collective framing, humor that doesn't survive translation, and the unspoken "would a local actually post this?" test.

---

## See it work

**Input** — an English Twitter/X hot take:

> "Hot take: everyone's obsessed with NVIDIA but the real AI trade is power & cooling. You can't run a GPU you can't cool. Networking, energy, thermal — that's where the next 10x is hiding. NVDA is consensus. The picks-and-shovels layer underneath it isn't."

**Output** — rebuilt for Xiaohongshu (小红书):

> 🔥 说个有点反共识的观点：大家都在盯着英伟达，但AI真正的机会其实在「电力」和「散热」👀
>
> 逻辑很简单——GPU再强，散不了热也跑不起来⚡️
>
> 网络、能源、散热… 这些「卖铲子」的环节才是下一个10倍藏的地方💰
>
> 英伟达已经是共识了，但它脚下那一层，还没什么人讨论。
>
> 姐妹们怎么看？评论区聊聊～👇
>
> #AI投资 #英伟达 #美股 #投资笔记 #散户日记

It didn't translate the words. It changed structure, pacing, emoji norms, and added the community hook XHS posts live on — because that's what a native would do.

---

## What it handles

**Cultural spheres:** English ↔ Chinese ↔ Japanese, any direction

**Platform registers:** LinkedIn · Xiaohongshu (小红书) · Weibo · Twitter/X · Instagram · Japanese formal/business · Japanese casual

---

## Quality gate (bundled)

Ships with `scripts/validate.py` — a heuristic checker that catches "this is secretly a literal translation" smells before you post: missing platform markers (emoji/hashtags on XHS, line breaks on LinkedIn, keigo on formal JP), wrong-language output, and structure that mirrors the source 1:1.

```bash
python scripts/validate.py --target xhs --source source.txt --adapted adapted.txt
```

Targets: `xhs` · `weibo` · `linkedin` · `twitter` · `jp_formal` · `jp_casual`. Pure Python 3, no dependencies. It flags smells; the native-fluency call stays human.

---

## How to use it

Once installed, just ask Claude naturally:

- *"Post this on Xiaohongshu"*
- *"Make this sound natural in Japanese"*
- *"Rebuild this Chinese post for an English audience"*
- *"Adapt this announcement across all three of my markets"*

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
