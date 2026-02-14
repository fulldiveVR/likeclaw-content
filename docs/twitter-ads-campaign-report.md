# Twitter/X Ad Campaigns — Setup Report

*Created: February 13, 2026*
*Platform: ads.x.com*
*Account: @alex_y_su*
*Status: All campaigns saved as DRAFT (not launched)*

---

## Summary

5 campaigns created following the plan in `marketing/twitter-ads.md`. Each campaign has one ad variant (the "A" copy) with a website card pointing to `likeclaw.com/#early-access`. All are saved as drafts pending review before launch.

| # | Campaign Name | Angle | Ad Group | Budget | Goal |
|---|--------------|-------|----------|--------|------|
| 1 | LikeClaw - C1 Security | OpenClaw security problems | Security Angle | $15/day | Link clicks |
| 2 | LikeClaw - C2 Cost | Subscription stacking / surprise bills | Cost Angle | $15/day | Link clicks |
| 3 | LikeClaw - C3 Setup | 3 days vs 30 seconds | Setup Speed | $15/day | Link clicks |
| 4 | LikeClaw - C4 Multi-Model | One account, all models | Multi-Model Access | $15/day | Link clicks |
| 5 | LikeClaw - C5 Direct | Broad positioning | Direct Response | $15/day | Link clicks |

**Common settings across all campaigns:**
- Objective: Website traffic
- Goal: Link clicks
- Bid strategy: Autobid
- Location: United States
- Gender: Any
- Age: All ages
- Pacing: Standard
- Placements: Home timelines, Profiles, Search results, Replies

---

## Campaign 1: Security

**Ad group name:** Security Angle
**Daily budget:** $15.00
**Audience size:** ~1.4M-1.6M

**Keywords (5):**
- openclaw security
- ai agent malware
- openclaw malicious
- ai agent risk
- mcp security

**Follower look-alikes (5):**
- @OpenClawAI
- @snaborern (Snyk)
- @kaspersky
- @waboriz
- @baboright (Bitsight)

**Ad: Security 1A - Malicious Skills**

> 341 malicious skills. Plaintext API keys. Raw system access to your machine.
>
> That's OpenClaw's security model.
>
> LikeClaw runs every task in an isolated sandbox. Container created, task runs, container destroyed. Your machine never touched.
>
> 30 seconds to try it.

**Headline:** Sandboxed AI agents. Your machine never touched.
**URL:** https://likeclaw.com/#early-access

---

## Campaign 2: Cost

**Ad group name:** Cost Angle
**Daily budget:** $15.00
**Audience size:** ~1.2M-1.4M

**Keywords (5):**
- ai subscription
- api costs
- chatgpt expensive
- ai subscription cancel
- ai tools cost

**Follower look-alikes (5):**
- @OpenAI
- @AnthropicAI
- @cursor_ai
- @ChatGPTapp
- @typingmind

**Ad: Cost 2A - Subscription Stack**

> ChatGPT Plus: $20/mo
> Claude Pro: $20/mo
> Gemini: $20/mo
> Cursor: $20/mo
>
> That's $80/mo before you run a single AI agent task. 42% of that spend is wasted.
>
> LikeClaw: one account, 100+ models, pay per task. Set a $10 cap and see how far it goes.

**Headline:** One account. 100+ models. Pay per task.
**URL:** https://likeclaw.com/#early-access

---

## Campaign 3: Setup / Speed

**Ad group name:** Setup Speed
**Daily budget:** $15.00
**Audience size:** ~1.2M-1.5M

**Keywords (5):**
- ai tools easy
- no code ai
- ai agent setup
- ai automation simple
- ai no setup

**Follower look-alikes (4):**
- @ProductHunt
- @indiehackers
- @YCombinator
- @_buildspace

**Ad: Setup 3A - 30 Seconds**

> OpenClaw: 3+ days to set up. Docker, dependencies, config files, API keys, permission management.
>
> LikeClaw: open browser, sign up, run your first task. 30 seconds.
>
> Same capabilities. No terminal required.

**Headline:** From signup to first AI agent task in 30 seconds.
**URL:** https://likeclaw.com/#early-access

---

## Campaign 4: Multi-Model

**Ad group name:** Multi-Model Access
**Daily budget:** $15.00
**Audience size:** ~1.2M-1.4M

**Keywords (5):**
- claude vs gpt
- best ai model
- ai model comparison
- multi model
- which ai model

**Follower look-alikes (4):**
- @AnthropicAI
- @GoogleAI
- @deepseek_ai
- @OpenRouterAI

**Ad: Multi-Model 4A - One Account**

> Claude for code review. GPT-4 for docs. Gemini for large context. DeepSeek for batch processing.
>
> One account. 100+ models. See the cost before every run. Switch models per task.
>
> Stop paying $20/mo to four providers for things you use 42% of.

**Headline:** One account. 100+ models. Pay per task.
**URL:** https://likeclaw.com/#early-access

---

## Campaign 5: Direct Response

**Ad group name:** Direct Response
**Daily budget:** $15.00
**Audience size:** ~1.2M-1.4M

**Keywords (4):**
- ai agent
- ai automation
- ai tools 2026
- ai assistant

**Follower look-alikes (5):**
- @OpenAI
- @AnthropicAI
- @GoogleAI
- @ProductHunt
- @deepseek_ai

**Ad: Direct 5A - Broad**

> AI agents that actually do things — without wrecking your machine.
>
> Sandboxed execution. 100+ models. Pay per task from $0.001. Running in 30 seconds.
>
> Free credits to start. No credit card.

**Headline:** AI agents that work. Without wrecking your machine.
**URL:** https://likeclaw.com/#early-access

---

## Known Issues

1. **Placeholder image on all ads.** All 5 campaigns use "Untitled Nov 16, 2022" from the existing media library — the only image with a valid aspect ratio. This needs to be replaced with proper LikeClaw creatives before launch.

2. **"Display creatives: 0" on review pages.** Appeared on Campaigns 2, 3, and 4 review screens. This is a display issue in the campaign form — the ads are saved correctly and visible in Ads Manager.

3. **Single ad variant per campaign.** Only the "A" variant was created for each campaign. Per the A/B testing plan, B/C/D variants should be added during Week 2 after identifying winning angles.

---

## Before Launch Checklist

- [ ] Upload proper ad images (1200x675px, 16:9, PNG/JPG) for each campaign
- [ ] Replace placeholder image in all 5 campaigns
- [ ] Install X Pixel on likeclaw.com for conversion tracking
- [ ] Create "EarlyAccessSignup" conversion event
- [ ] Set optimization goal to "Conversions" (currently "Link clicks" for testing)
- [ ] Review all ad copy for final approval
- [ ] Verify landing page (likeclaw.com/#early-access) is live and working
- [ ] Set campaign start dates (currently starts immediately when launched)
- [ ] Launch Week 1 ads: one ad per campaign (1A, 2A, 3A, 4A, 5A) at equal budget

## Recommended Screenshots for Ad Images

| Campaign | What to screenshot | Why |
|----------|-------------------|-----|
| C1: Security | Sandbox/container execution view showing isolation | Visually communicates the security model |
| C2: Cost | Cost preview before a task runs (showing $0.02 etc.) or spending cap settings | Reinforces "see the cost before every run" |
| C3: Setup | First screen after signup — the task creation interface | Visually contrasts with terminal/config complexity |
| C4: Multi-Model | Model picker dropdown showing Claude, GPT-4, Gemini, DeepSeek with prices | Most visually distinctive differentiator |
| C5: Direct | Completed task with visible results (code output, generated file) | Shows "this actually does things" |

Image spec: 1200x675px (16:9), PNG or JPG, max 5MB.

---

## Budget Summary

| Phase | Duration | Daily spend | Total |
|-------|----------|-------------|-------|
| Week 1: Angle testing | 7 days | $15 | $105 |
| Week 2: Copy testing | 7 days | $15 | $105 |
| Week 3: Scaling | 7 days | $20 | $140 |
| **Total test** | **21 days** | | **$350** |

Expected results at $3-5 CPA: 70-115 early access signups from a $350 test budget.

---

## A/B Testing Plan (from marketing/twitter-ads.md)

**Week 1:** Run one ad per campaign (1A, 2A, 3A, 4A, 5A). Equal budget. Kill any ad with CPA > $5 after 72 hours and $15+ spend. Note any ad with CPA < $3 as a winner.

**Week 2:** Take the 2 best angles. Run all 4 variants (A/B/C/D) for each. Pause losers after 48 hours.

**Week 3:** Double budget on top 2-3 ads. Test new audience segments.
