# Product Marketing Context

*Last updated: February 12, 2026*

## Product Overview
**One-liner:** Your AI assistant that actually does things — no setup, no security nightmares, no surprise bills.
**What it does:** AI Wize is a cloud-native AI agent platform that gives users sandboxed code execution, any LLM model, a vetted skills marketplace, persistent file systems and workspaces — running in 30 seconds, not 3 days. Everything OpenClaw promised, delivered as a service.
**Product category:** Cloud AI Personal Assistant / AI Agent Platform
**Product type:** SaaS (cloud-hosted)
**Business model:** Freemium with tiered subscriptions
- Free: $0/mo — 50 tasks, basic models, 1 workspace
- Pro: $15-20/mo — unlimited chat, 500 sandbox executions, all models, 5 workspaces
- Power: $40/mo — unlimited everything, BYOK, priority execution
- Team: $25/seat/mo — Power features + team management, SSO

## Target Audience
**Target companies:** Startups, small-to-medium businesses, individual developers, technical founders, non-technical business users wanting AI automation
**Decision-makers:** Individual users (PLG), technical leads, founders, operations managers
**Primary use case:** Running autonomous AI agents safely in the cloud without local setup, security risks, or unpredictable costs
**Jobs to be done:**
- "I need an AI agent that can execute code and automate tasks without spending 3 days setting it up"
- "I want to use AI agents without worrying they'll compromise my system or rack up surprise bills"
- "I need access to multiple AI models without paying $20/month to each provider separately"
**Use cases:**
- Automated code execution and development tasks
- Data processing and analysis in sandboxed environments
- Multi-model AI workflows (Claude, GPT-4, Gemini, DeepSeek)
- Task automation via vetted skills marketplace
- Team collaboration on AI-powered workspaces

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| OpenClaw Refugee (Developer) | Security, cost control, reliability | Spent 3 days setting up OpenClaw, hit security warnings, got $300+ bills | Zero setup, sandboxed security, predictable pricing |
| AI-Curious Developer | Getting started fast, model flexibility, no vendor lock-in | Overwhelmed by options, doesn't want to commit to one provider | One subscription, every model, running in 30 seconds |
| Non-Technical Founder | Automation without coding, safety, simplicity | Wants AI automation but scared of terminal setup and security risks | Browser-based, no-code AI agent that just works |
| Team Lead / Operations | Collaboration, governance, audit trail | No team-friendly AI agent tools with proper access controls | Multi-tenant workspaces, SSO, usage tracking |

## Problems & Pain Points
**Core problem:** Autonomous AI agents today force users to choose between power (OpenClaw — full system access, complex setup, security nightmares) and safety (ChatGPT — limited, can't actually execute things). There's no middle ground.
**Why alternatives fall short:**
- OpenClaw: 3+ days to set up, raw system access = security nightmare (Kaspersky, Cisco, Snyk, Wiz all issued warnings), 341+ malicious skills found, runaway costs ($50-750/mo), "I ship code I don't read" founder philosophy
- ChatGPT/Claude/Gemini: Chat-only interfaces that can't truly execute code, automate workflows, or act autonomously
- Cursor/Copilot: IDE-locked, coding-only, not general-purpose agents
- Self-hosted (Open WebUI, LobeChat): Require technical setup, no sandboxed execution
**What it costs them:** 3+ days of setup time, $50-750/mo in unpredictable API costs, security vulnerabilities exposing their entire system, context-switching between 3-4 AI subscriptions averaging $133/mo
**Emotional tension:** Fear of security breaches, frustration with complex setup, anxiety about surprise bills, FOMO on AI agent capabilities

## Competitive Landscape
**Direct:** OpenClaw — falls short because of catastrophic security model (341 malicious skills, plaintext API keys, RCE vulnerabilities), 3-day setup, unpredictable costs ($50-750/mo), and "I ship code I don't read" development philosophy
**Secondary:** ChatGPT / Claude / Gemini chat interfaces — fall short because they can't execute code, run background tasks, or act autonomously. Limited to conversation, not action.
**Indirect:** Cursor / GitHub Copilot / Bolt.new — fall short because they're locked to specific workflows (coding, UI generation) rather than being general-purpose AI agents

## Differentiation
**Key differentiators:**
- Zero setup: Running in 30 seconds vs. 3 days (cloud-native, browser-based)
- Sandboxed execution: E2B containers vs. raw system access (real security)
- Vetted skills marketplace: Mandatory security review vs. open registry with 341+ malicious skills
- Predictable pricing: Fixed tiers vs. runaway API costs
- Multi-model: One subscription covers Claude, GPT-4, Gemini, DeepSeek — no vendor lock-in
- Team-ready: Multi-tenant workspaces, auth, billing from day one
**How we do it differently:** Cloud-native architecture with E2B sandboxed containers. Every skill is vetted before publishing. Usage is metered and capped per tier. All models accessible through one unified interface.
**Why that's better:** Users get the power of autonomous AI agents (code execution, file system, automation) with the safety of a managed cloud service (sandboxed, vetted, predictable).
**Why customers choose us:** "I want OpenClaw's capabilities without OpenClaw's problems."

## Objections
| Objection | Response |
|-----------|----------|
| "I can just self-host OpenClaw for free" | You can — if you have 3 days for setup, tolerance for 341+ malicious skills, comfort with raw system access to your machine, and budget for $50-750/mo in surprise API costs. We built what OpenClaw should have been. |
| "How is this different from ChatGPT Plus?" | ChatGPT talks. We do. Sandboxed code execution, persistent file system, autonomous task running, skills marketplace — ChatGPT can't execute code on your behalf or run background automations. |
| "Is my data safe in the cloud?" | Safer than on your local machine with OpenClaw. Every execution runs in an isolated E2B sandbox that's destroyed after use. Your data never touches other users' environments. We support BYOK for full control. |

**Anti-persona:** Users who need fully offline/air-gapped AI (government, classified). Users who want to build and sell their own AI agent platform. Users who need 100% open-source with self-hosting only.

## Switching Dynamics
**Push:** Security warnings from Kaspersky/Cisco/Snyk about OpenClaw. Surprise $300+ monthly bills. 3-day setup frustration. Malicious skills infecting systems.
**Pull:** 30-second setup. Predictable pricing. "Sleep at night" security. All models in one place. No vendor lock-in with BYOK.
**Habit:** Already invested time configuring OpenClaw. Familiar with local-first workflow. Existing skills/extensions built for OpenClaw ecosystem.
**Anxiety:** "Will it be as powerful as running locally?" "Can I migrate my OpenClaw workflows?" "What if the company shuts down and I lose access?"

## Customer Language
**How they describe the problem:**
- "I spent 3 days configuring this thing and lost $50 in tokens before it did anything useful"
- "It's a security nightmare — it has full access to my machine"
- "I'm paying $20 to OpenAI + $20 to Anthropic + $20 to Google and only using 42% of what I'm paying for"
- "Simpler alternatives cover 99% of what they actually need"
- "Please stop using OpenClaw" (XDA-Developers headline)
- "A disaster waiting to happen" (Gary Marcus)
**How they describe us:**
- "What OpenClaw should have been"
- "OpenClaw but in the cloud with actual security"
- "One subscription, every model"
**Words to use:** sandboxed, zero-setup, predictable, vetted, secure, instant, cloud-native, multi-model, BYOK
**Words to avoid:** revolutionary, disruptive, game-changing, AI-powered (everything is), innovative, cutting-edge, next-generation, leverage, synergy
**Glossary:**
| Term | Meaning |
|------|---------|
| E2B sandbox | Isolated cloud container for safe code execution |
| BYOK | Bring Your Own Key — use your own API keys for full control |
| Skills | Pre-built automation packages (like plugins/extensions) |
| Workspace | Persistent environment with files, history, and configuration |

## Brand Voice
**Tone:** Confident, direct, slightly irreverent. Not corporate. Not try-hard startup. Think "engineer who's been through it and built something better."
**Style:** Short sentences. Specific claims with evidence. No fluff. Comparison-driven (show, don't tell). Occasional dry humor.
**Personality:** Competent, trustworthy, pragmatic, no-BS, builder-first

## Proof Points
**Metrics:**
- 30-second setup vs. 3-day OpenClaw setup (verified)
- 341+ confirmed malicious skills in OpenClaw's marketplace (Snyk research, Feb 2026)
- 36% of OpenClaw skills contain prompt injection (Snyk)
- $50-750/mo OpenClaw cost range vs. $0-40/mo predictable tiers
- OpenClaw: 5 name changes in 3 months
**Customers:** Private beta (testimonials to come)
**Testimonials:**
> Pending — private beta stage
**Value themes:**
| Theme | Proof |
|-------|-------|
| Security | E2B sandboxed execution vs. OpenClaw's 341 malicious skills, plaintext API keys, and RCE vulnerabilities |
| Zero friction | 30-second cloud setup vs. 3-day local installation |
| Cost predictability | Fixed tiers ($0-40/mo) vs. runaway costs ($50-750/mo documented) |
| Multi-model freedom | One subscription for Claude + GPT-4 + Gemini + DeepSeek vs. $20/mo each |

## Goals
**Business goal:** Build waitlist/early access list for private beta, targeting 1,000+ signups in month 1
**Conversion action:** Early access signup (email + optional use case)
**Current metrics:** Pre-launch — no baseline yet. Targeting 1,000+ signups month 1, 100+ active beta users.

## Reference Case Studies
- **Cursor:** $0 to $1B ARR in 24 months — PLG, 2K free completions, bottom-up enterprise
- **Bolt.new:** $80K/yr to $40M ARR in 5 months — zero friction, single tweet launch, <40 employees
- **Perplexity:** 0 to 45M users, $20B valuation — category creation, strategic partnerships
- **OpenClaw:** 0 to 150K stars in 10 weeks — open source virality, but now facing massive security backlash

## Market Context
- Market size: $3.35B (2025) → $21.11B (2030) at 44.5% CAGR
- Agentic AI is the dominant paradigm shift (Gartner: 40% of enterprise apps by end 2026)
- OpenClaw security backlash peaking Feb 2026 — perfect timing window
- Multi-model access is table stakes
- Zero-friction onboarding is proven GTM strategy
