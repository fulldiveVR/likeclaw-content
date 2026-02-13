# OpenClaw Deep Research Report

## Date: February 2026

---

## 1. What is OpenClaw?

OpenClaw is a **free and open-source autonomous AI agent** that runs on your own hardware (Mac Mini, Raspberry Pi, cloud server, etc.) and acts as a personal AI assistant. Unlike ChatGPT or Claude which are web-based chat interfaces, OpenClaw is a **long-running process** that lives on your machine, has genuine system access (shell, filesystem, scripts), and can act autonomously — monitoring situations, executing tasks, and taking action without being prompted.

It connects to the LLM of your choice (Claude, GPT-4, DeepSeek, or local models via Ollama) and exposes itself through **15+ messaging platforms** you already use: WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Google Chat, Microsoft Teams, Matrix, and more.

Key capabilities:
- Auto-processing emails, sending responses
- Calendar management, flight check-ins
- Writing and executing code on your machine
- Browser automation with screenshots
- Daily briefings pulling data from multiple sources
- Background monitoring and autonomous action

Sources: [OpenClaw Official Site](https://openclaw.ai/) | [DigitalOcean Overview](https://www.digitalocean.com/resources/articles/what-is-openclaw) | [Turing College Blog](https://www.turingcollege.com/blog/openclaw)

---

## 2. Naming History: Clawdbot / Moltbot / OpenClaw

These are all **the same project** at different points in its evolution:

| Date | Name | Why |
|------|------|-----|
| Nov 2025 | **Warelay** | Original release |
| Late 2025 | **Clawdis** | First rename |
| Late 2025 | **Clawdbot** | Play on "Claude" + "claw" (lobster mascot) — this is the name that went viral |
| Jan 27, 2026 | **Moltbot** | Renamed after **Anthropic sent a trademark cease-and-desist** (too similar to "Claude"). "Molt" = lobster shedding its shell |
| Jan 30, 2026 | **OpenClaw** | Final name. Steinberger said "Moltbot never quite rolled off the tongue" |

The project was renamed **5 times** in under 3 months. The Anthropic C&D paradoxically amplified growth — 91,000 additional stars in the 72 hours surrounding the controversy.

Sources: [CNBC Coverage](https://www.cnbc.com/2026/02/02/openclaw-open-source-ai-agent-rise-controversy-clawdbot-moltbot-moltbook.html) | [Growth Case Study](https://growth.maestro.onl/en/articles/openclaw-viral-growth-case-study)

---

## 3. Value Proposition

OpenClaw's pitch boils down to:

1. **Local-first privacy**: Everything runs on your hardware. No corporate servers mining your data. No ToS changes.
2. **True autonomy**: Unlike ChatGPT which only responds when prompted, OpenClaw can monitor, anticipate, and execute autonomously.
3. **Multi-channel**: Talk to your AI from whatever app you already use. Unified conversation history across all channels.
4. **Open source & free**: MIT license. You only pay for LLM API costs.
5. **Extensible**: 5,705+ community skills on ClawHub registry.
6. **System-level access**: It can actually *do things* — run scripts, modify files, execute commands — not just talk about doing them.

The tagline: "The AI Assistant That Actually Does Things."

Sources: [Clawbot.ai](https://clawbot.ai/) | [MacStories Review](https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/)

---

## 4. Tech Stack & Architecture

| Component | Technology |
|-----------|-----------|
| **Language** | TypeScript (~188,500 lines of code, though some reports say 430,000+ including all packages) |
| **Core** | Long-running CLI process + WebSocket Gateway (port 18789) |
| **Concurrency** | "Lane Queue" system — serial execution by default to prevent race conditions |
| **Memory** | Dual system: **Vector Search** (semantic recall) + **SQLite FTS5** (keyword precision). Markdown files are canonical source, SQLite stores chunked embeddings |
| **Storage** | JSONL session files, local filesystem |
| **Channel Adapters** | Built-in: `src/telegram/`, `src/discord/`, `src/slack/`, `src/imessage/`, etc. Plus extensible channel plugins |
| **Plugin System** | Plugin loader (`src/plugins/loader.ts`) scans workspace packages for `openclaw.extensions` field in `package.json`, validates against schemas, hot-loads |
| **LLM Integration** | Provider-agnostic — Claude, GPT-4, DeepSeek, local Ollama models |
| **Security** | Allowlist-based command approval + structure-based blocking (parses shell AST to block dangerous patterns like redirections) |
| **License** | MIT |

Architecture highlights:
- WebSocket Gateway coordinates all clients (phone, CLI, web UI)
- Multi-channel adapters ship built-in and can be added via plugins
- Per-session snapshots cache available skills and their content
- Memory system uses JSONL for persistence with vector+keyword hybrid search

Sources: [Architecture Guide](https://ppaolo.substack.com/p/openclaw-system-architecture-overview) | [Memory Architecture](https://www.mmntm.net/articles/openclaw-memory-architecture) | [GitHub Repo](https://github.com/openclaw/openclaw)

---

## 5. Skills / Extensions System (ClawHub)

**Structure**: Each skill is a lightweight package — a folder containing a **`SKILL.md`** file plus supporting resources. The SKILL.md uses YAML frontmatter for metadata and markdown for instructions.

**Discovery pipeline**:
1. Skills discovered from bundled (`skills/`), workspace (`~/.openclaw/workspace/skills/`), and managed install locations
2. YAML frontmatter extracted and validated against skill metadata schema
3. Requirements checked (binaries on PATH, env vars, config sections, OS platform)
4. Valid skills added to `SkillsRegistry`
5. Per-session snapshots cache available skills

**ClawHub Registry**:
- Open registry — anyone with a GitHub account 1+ weeks old can publish
- **5,705 community-built skills** as of Feb 7, 2026
- Categories span: crypto trading, DeFi, automation, Reddit insights, social media, productivity
- No adequate vetting or code review for submissions (root cause of malicious skills problem)

**Security nightmare**: Researchers found **341 malicious skills** on ClawHub, with 335 using fake prerequisites to install macOS stealer malware (Atomic Stealer / AMOS). Snyk found prompt injection in 36% of skills analyzed. Cisco demonstrated data exfiltration via a third-party skill.

Sources: [ClawHub GitHub](https://github.com/openclaw/clawhub) | [Skills Docs](https://docs.openclaw.ai/tools/skills) | [The Hacker News - 341 Malicious Skills](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) | [Snyk ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)

---

## 6. Pricing Model

**Software**: Completely free and open source (MIT).

**Actual costs for users**:

| Cost Category | Range |
|--------------|-------|
| Casual personal use | $5-20/month (LLM API fees) |
| Power users | $50-100/month |
| Heavy usage (like Federico Viticci's 180M tokens) | ~$3,600/month |
| Hardware (if self-hosting) | $0 (existing machine) to $500+ (dedicated Mac Mini/GPU box) |
| Local LLM via Ollama | $0 API cost but requires expensive GPU hardware |

The expensive operations are browser automation (vision model calls per screenshot) and long autonomous sessions that burn through tokens.

**Project revenue**: OpenClaw accepts GitHub sponsors with lobster-themed tiers: "Krill" ($5/mo) to "Poseidon" ($500/mo). Steinberger says he "doesn't keep sponsorship funds" and is "figuring out how to pay maintainers properly — full-time if possible."

Sources: [Pricing Guide](https://www.eesel.ai/blog/openclaw-ai-pricing) | [Cost Analysis](https://yu-wenhao.com/en/blog/2026-02-01-openclaw-deploy-cost-guide/) | [$47/week Review](https://medium.com/@likhitkumarvp/i-spent-47-testing-openclaw-for-a-week-heres-what-s-actually-happening-c274dc26a3fd)

---

## 7. Community & User Base

**GitHub Stats** (as of early Feb 2026):
- **145,000-157,000 stars** (reports vary by date)
- **16,100-20,000+ forks**
- **339+ contributors**
- **416,000+ npm downloads** (30-day period ending early Feb 2026)
- **2 million website visits** in one week after the Jan 30 rebrand

**Growth velocity**: 34,168 stars in 48 hours at peak (~710 stars/hour). 18x faster than Kubernetes's historical growth rate.

**Community hubs**:
- **Discord**: Most active hub. "Claw Crew" contributors for real-time discussions, troubleshooting, skill sharing
- **Twitter/X**: Community account at [@OpenClawCommunity](https://x.com/i/communities/2013441068562325602). Heavy crypto Twitter adoption
- **Reddit**: Active in r/AIAgents and related subs
- **Moltbook**: The AI social network with 770,000-1.5M+ active agents (bots posting and interacting with each other)

**Actual usage vs hype**: Media reports note that "actual and active usage figures remain unclear" despite massive star counts. Many HN users reported they "couldn't find a single user of OpenClaw in their familiar communities."

Sources: [GitHub Stars Case Study](https://growth.maestro.onl/en/articles/openclaw-viral-growth-case-study) | [150K Stars Article](https://www.arturmarkus.com/openclaw-hits-150000-github-stars-in-10-weeks-open-source-ai-assistant-overtakes-major-projects-with-416000-npm-downloads/) | [TrendingTopics.eu](https://www.trendingtopics.eu/openclaw-2-million-visitors-in-a-week/)

---

## 8. User Sentiment

### Positive (Twitter/X, early adopters)
- "Nothing short of an iPhone moment"
- "Genuinely feels like early AGI"
- "It is getting essential to my daily life"
- "What Apple Intelligence should have been"

### Negative (Reddit, HN, security researchers)
- **Cost horror stories**: Users reporting $300-750/month, Viticci burned $3,600 in month one
- **Setup pain**: "I spent three days configuring Moltbot and lost $50 in tokens. I switched to Claude Code and finished the project in an hour."
- **Security terror**: Kaspersky, Cisco, Snyk, Wiz, Bitsight all published warnings
- **Hype vs reality**: "Simpler alternatives cover 99% of what they actually need"
- **XDA-Developers**: Published article titled "Please stop using OpenClaw"
- **Computerworld**: Called it "a security nightmare"
- **Gary Marcus**: "A disaster waiting to happen"

### HN consensus
Developers on HN were split. Some loved it for personal automation. Many found that for code-related tasks, "models often fail or try to shortcut tasks." The security concerns dominated most threads.

Sources: [HN - Real Users Thread](https://news.ycombinator.com/item?id=46838946) | [XDA - Stop Using OpenClaw](https://www.xda-developers.com/please-stop-using-openclaw/) | [Platformer Review](https://www.platformer.news/moltbot-clawdbot-review-ai-agent/) | [Gary Marcus](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere)

---

## 9. Pain Points Users Complain About

1. **Security is a dumpster fire**: Plaintext API keys in `~/.clawdbot`, prompt injection via email, 341+ malicious skills on ClawHub, one-click RCE vulnerability, exposed instances leaking data
2. **Runaway costs**: No cost controls by default, browser automation eats tokens, users unknowingly burning $50-100+/month
3. **Setup complexity**: Requires local env setup, dependency management, permission config. Not plug-and-play
4. **Overhyped**: Star count doesn't reflect actual active usage. Many people star it but never get it running
5. **Reliability**: Models fail on complex tasks, try to shortcut, and sometimes take destructive actions
6. **Name confusion**: 5 renames in 3 months made it hard to follow or search for help
7. **Supply chain attacks**: Open skill registry with no vetting is a malware vector
8. **Credential management**: Keys stored insecurely, deleted keys found in .bak files

Sources: [Snyk Security Analysis](https://snyk.io/articles/clawdbot-ai-assistant/) | [Kaspersky Blog](https://www.kaspersky.com/blog/openclaw-vulnerabilities-exposed/55263/) | [The Register](https://www.theregister.com/2026/02/05/openclaw_skills_marketplace_leaky_security/) | [Cisco Blog](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare)

---

## 10. Launch / Growth Story

**Timeline**:
- **Nov 2025**: Peter Steinberger releases "Warelay" — a personal AI project
- **Late 2025**: Renames to Clawdis, then Clawdbot. Starts gaining traction in dev communities
- **Jan 27, 2026**: Anthropic C&D. Renamed to Moltbot in a 5 AM Discord brainstorm
- **Jan 28, 2026**: Matt Schlicht launches **Moltbook** — AI social network for bots. Goes viral
- **Jan 29-30, 2026**: Peak growth. 34,168 stars in 48 hours
- **Jan 30, 2026**: Renamed to OpenClaw. Crosses 100K stars same day
- **Feb 2026**: 150K+ stars, massive media coverage (CNBC, CNN, Fortune, Scientific American, TechCrunch), security backlash begins

**Growth drivers**:
1. Open source + free (MIT license)
2. Moltbook virality (AI bots creating religions and "dealing digital drugs" made headlines)
3. Anthropic trademark drama (Streisand effect)
4. Crypto Twitter adoption
5. Genuine technical innovation (multi-channel AI agent with system access)
6. China adoption (Alibaba, Tencent, ByteDance integrations)

Sources: [CNBC](https://www.cnbc.com/2026/02/02/openclaw-open-source-ai-agent-rise-controversy-clawdbot-moltbot-moltbook.html) | [CNN Moltbook Explainer](https://www.cnn.com/2026/02/03/tech/moltbook-explainer-scli-intl) | [Growth Case Study](https://growth.maestro.onl/en/articles/openclaw-viral-growth-case-study)

---

## 11. Founder / Team

**Peter Steinberger** (creator):
- Austrian developer, studied at Vienna University of Technology
- Founded **PSPDFKit** — a PDF SDK used by Dropbox, Autodesk, etc.
- Sold PSPDFKit to Insight Partners for **$100M+** (majority sale)
- Post-exit: "celebrating, traveling, therapy, experiments with ayahuasca" (his words)
- After a 3-year break, returned to building with LLMs
- Self-describes as a "vibe coder" — famously said **"I ship code I don't read"**
- The project is not VC-funded. Runs on GitHub sponsorships

**Key ecosystem figures**:
- **Matt Schlicht**: Launched Moltbook (the AI social network). Tech entrepreneur, separate from Steinberger
- **339+ GitHub contributors**: Community-driven development
- No traditional "team" — it's an open source project with one primary maintainer and community contributors

Sources: [Pragmatic Engineer Interview](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code) | [Creator Economy Profile](https://creatoreconomy.so/p/how-openclaws-creator-uses-ai-peter-steinberger) | [TrendingTopics Vienna Event](https://www.trendingtopics.eu/openclaw-vienna-celebrate-peter-steinberger/)

---

## 12. GitHub Presence

| Metric | Value |
|--------|-------|
| Stars | ~145,000-157,000 |
| Forks | 16,100-20,000+ |
| Contributors | 339+ |
| Lines of Code | ~188,500 (core) / 430,000+ (full) |
| Language | TypeScript |
| License | MIT |
| npm Downloads (30-day) | 416,000+ |
| ClawHub Skills | 5,705 |
| Growth Rate | 1,667 stars/day over 60 days (18x Kubernetes) |
| Peak Growth | 34,168 stars in 48 hours |

**Notable forks/derivatives**:
- **NanoClaw**: 700 lines of TypeScript. Runs in Apple containers for security. Built on Anthropic Agents SDK
- **Nanobot**: 4,000 lines of Python (99% smaller). University of Hong Kong project
- **Moltworker**: Cloudflare Workers deployment (by Cloudflare themselves)
- **openclaw-coolify**: One-click self-hosted deployment
- **openclaw-secure-stack**: Hardened deployment with skills scanner and prompt injection protection

Sources: [GitHub Repo](https://github.com/openclaw/openclaw) | [NanoClaw](https://github.com/qwibitai/nanoclaw) | [Nanobot](https://github.com/HKUDS/nanobot) | [Cloudflare Moltworker](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/)
