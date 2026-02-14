# Twitter/X Origin Story Campaign — "Why We Built LikeClaw"

*Created: February 13, 2026*
*Type: Organic content (building in public)*
*Goal: Establish founder credibility, explain the B2B-to-B2C pivot, attract early adopters*
*Post from: Founder's personal account + @LikeClawAI*

---

## The Narrative Arc

We had an enterprise B2B product (AI Wize) — a control panel for AI agents with background tasks, sandboxed execution, security controls, approval workflows, audit trails. Built for enterprises.

Then OpenClaw happened. 150K GitHub stars in 10 weeks. Consumer demand for autonomous AI agents was undeniable.

We realized: we already had the infrastructure. We just needed to strip the enterprise layer and ship a consumer product. No approval workflows. No audit trails. No multi-tenant governance. Just the raw, secure AI agent experience.

That's LikeClaw — enterprise infrastructure, consumer simplicity.

---

## Thread 1: The Origin Story (flagship, pin this)

**Post from: Founder's personal account**

### Tweet 1/9 (hook)

We spent 2 years building AI agent infrastructure for enterprises.

Then OpenClaw got 150K GitHub stars in 10 weeks and we realized something.

Here's why we built LikeClaw, and what it has to do with our B2B product:

### Tweet 2/9

Our B2B product (AI Wize) is a control panel for AI agents. Background task execution. Sandboxed containers. Security policies. Approval workflows. Audit trails. SSO. The works.

Built for CTOs who need AI agents running in production without keeping them up at night.

### Tweet 3/9

Then OpenClaw happened.

150K stars. 5 name changes. Kaspersky, Cisco, Snyk all publishing security warnings. 341 malicious skills on their marketplace. Users spending $50-750/month with zero cost controls.

And people still couldn't stop using it.

### Tweet 4/9

That was the signal.

The demand for autonomous AI agents wasn't just an enterprise thing. Regular developers, founders, freelancers — everyone wanted AI that could actually execute code, automate tasks, and run in the background.

OpenClaw proved the demand existed. Despite everything.

### Tweet 5/9

We looked at what we had.

E2B sandboxed execution — already built.
Multi-model routing (100+ models) — already built.
Vetted skills marketplace — already built.
Persistent workspaces — already built.
Background task execution — already built.

We just needed to remove the enterprise layer.

### Tweet 6/9

So we stripped it down.

No approval workflows. No granular permission matrices. No audit trail dashboards. No multi-tenant governance. No 30-page security questionnaires.

Just the raw experience: describe a task, pick a model, see the cost, run it. In a sandbox. In 30 seconds.

### Tweet 7/9

That's LikeClaw.

Enterprise-grade infrastructure underneath. Consumer-grade simplicity on top.

The same E2B containers that enterprises trust for production workloads — now available to anyone with an email address and 30 seconds.

### Tweet 8/9

The difference between us and OpenClaw isn't features. It's architecture.

OpenClaw gives an LLM raw access to your machine. We give it an isolated container that gets destroyed after every task.

Same capabilities. Fundamentally different risk profile.

### Tweet 9/9

We're in early access now.

Free credits at signup. No credit card. Set your own spending cap.

If you tried OpenClaw and got burned — or if you want what OpenClaw promised without the security nightmares — this is what we built.

likeclaw.com

---

## Thread 2: The "Why B2C" Decision (shorter, more personal)

**Post from: Founder's personal account**

### Tweet 1/5

Honest question we asked ourselves in December:

"Should we even do B2C? We have a perfectly good enterprise product."

The answer was in the data. Here's what convinced us:

### Tweet 2/5

OpenClaw hit 150K stars in 10 weeks. That's not enterprise demand. That's regular people wanting AI agents that actually do things.

But 341 malicious skills. Plaintext API keys. $3,600/month documented bills.

The demand was validated. The execution was broken.

### Tweet 3/5

We had the infrastructure to fix every single one of those problems. We'd already solved them for enterprises.

The question wasn't "can we build this?" It was "can we simplify it enough for someone who just wants to automate their email?"

### Tweet 4/5

Turns out, removing enterprise complexity is harder than adding it.

No approval workflows means the sandbox has to be bulletproof by default. No admin dashboards means spending caps have to be dead simple. No security team means the system has to be secure without configuration.

### Tweet 5/5

Six weeks later: LikeClaw.

Enterprise sandbox. Consumer UX. 30 seconds from signup to first task.

If you're the kind of person who tried OpenClaw and thought "this is amazing but terrifying" — we built this for you.

likeclaw.com

---

## Thread 3: The Technical Truth (for developer audiences)

**Post from: @LikeClawAI or Founder**

### Tweet 1/6

People ask how we built LikeClaw so fast.

We didn't. We spent 2 years building it for enterprises. Then we removed features.

A thread on what "enterprise infrastructure for consumers" actually means:

### Tweet 2/6

The sandbox:

Enterprise version: E2B containers with network policies, egress rules, CPU/memory quotas, custom runtimes, and integration with customer VPCs.

LikeClaw version: Same E2B container. Sensible defaults. You don't configure anything. It just works.

### Tweet 3/6

The model layer:

Enterprise version: SSO-gated model selection, per-team budgets, usage attribution, custom fine-tuned model endpoints, audit logging.

LikeClaw version: Pick a model from a dropdown. See the price. Run it. Set a monthly cap.

### Tweet 4/6

The skills marketplace:

Enterprise version: Private skill registry, code review pipeline, security scanning, version pinning, rollback controls.

LikeClaw version: Same security review pipeline. Same scanning. You just browse and install. We handle the vetting.

### Tweet 5/6

The pricing:

Enterprise version: Per-seat licensing, volume discounts, annual contracts, custom SLAs.

LikeClaw version: Pay per task. $0.001-$0.15 typical range. Set a $5 or $50 cap. Never go over.

### Tweet 6/6

Enterprise customers need 47 configuration options.

Consumer users need 3: what to do, which model, how much to spend.

LikeClaw is what happens when you build for the 3 and hide the 47.

likeclaw.com

---

## Standalone Tweets (daily content, mix into regular posting)

### Standalone 1: The One-Liner

We had a B2B AI agent platform. Then OpenClaw got 150K stars and proved everyone wants autonomous AI — not just enterprises.

So we stripped the enterprise layer and shipped the core: sandboxed execution, 100+ models, pay per task, 30 seconds to start.

That's LikeClaw.

### Standalone 2: The Realization

The moment we decided to build LikeClaw:

Reading a Reddit thread where someone spent 3 days setting up OpenClaw, lost $50 in tokens, and then their machine got flagged by their antivirus.

We had already solved every single one of those problems. For enterprises.

The consumer version took 6 weeks.

### Standalone 3: The Contrast

What enterprise AI agent infrastructure looks like:
- Approval workflows
- Audit trails
- SSO/SAML
- Per-team budgets
- Compliance dashboards

What consumers actually need:
- Does it work?
- Is it safe?
- How much does it cost?

We built both. LikeClaw is the second one.

### Standalone 4: The Market Signal

OpenClaw's growth wasn't surprising. The demand for AI agents that actually do things is real.

What was surprising: people tolerated 341 malicious skills, plaintext API keys, and $750/month bills just to get that experience.

Imagine what happens when the experience doesn't come with those tradeoffs.

### Standalone 5: The Builder Perspective

Building a consumer product from enterprise infrastructure is counterintuitive.

Everyone says "start simple, add complexity."

We did the opposite: start complex (enterprise), subtract complexity (consumer).

The advantage: the hard problems — security, isolation, cost control — were already solved.

### Standalone 6: Enterprise DNA

Every LikeClaw task runs in the same E2B sandbox architecture that our enterprise customers use for production AI workloads.

The difference: they configured it over 3 weeks with a DevOps team.

You get it in 30 seconds by clicking "Run."

### Standalone 7: The OpenClaw Acknowledgment

Credit where it's due: OpenClaw proved that regular people want AI agents that actually execute code and automate real work.

150K GitHub stars don't lie.

We just think it shouldn't require 3 days of setup, raw system access to your machine, and hope that none of the 341 malicious ClawHub skills end up on your system.

### Standalone 8: The Pivot Story (punchy)

2024: We build AI agent infrastructure for enterprises.
2025: OpenClaw goes viral. 150K stars. Everyone wants AI agents.
2026: We strip the enterprise layer. Ship LikeClaw. 30 seconds to your first AI agent task.

Sometimes the best product is the one you already built — minus the complexity.

### Standalone 9: Why Not Just Enterprise?

"Why not just focus on enterprise? That's where the money is."

Because the market for autonomous AI agents is going from $3.35B to $21.1B by 2030. Gartner says 40% of enterprise apps will embed AI agents by end of 2026.

The consumer wave is just starting. We'd rather be early.

### Standalone 10: The Security Story

Our enterprise customers have dedicated security teams reviewing our sandbox architecture.

LikeClaw users don't need one.

Same architecture. Same E2B isolation. Same encrypted credentials. Same container-per-task model.

The enterprise security team's job is already done. You get the result.

---

## Posting Strategy

### Week 1: Launch the narrative

| Day | Content | Account |
|-----|---------|---------|
| Mon | Thread 1 (Origin Story) — pin to profile | Founder |
| Tue | Standalone 4 (Market Signal) | @LikeClawAI |
| Wed | Standalone 2 (The Realization) | Founder |
| Thu | Standalone 7 (OpenClaw Acknowledgment) | @LikeClawAI |
| Fri | Thread 2 (Why B2C Decision) | Founder |

### Week 2: Build the technical credibility

| Day | Content | Account |
|-----|---------|---------|
| Mon | Thread 3 (Technical Truth) | Founder or @LikeClawAI |
| Tue | Standalone 6 (Enterprise DNA) | Founder |
| Wed | Standalone 3 (The Contrast) | @LikeClawAI |
| Thu | Standalone 5 (Builder Perspective) | Founder |
| Fri | Standalone 8 (The Pivot Story — punchy) | Founder |

### Week 3: Reinforce and engage

| Day | Content | Account |
|-----|---------|---------|
| Mon | Standalone 1 (One-Liner) | @LikeClawAI |
| Tue | Standalone 9 (Why Not Just Enterprise) | Founder |
| Wed | Standalone 10 (Security Story) | @LikeClawAI |
| Thu | Quote-tweet Thread 1 with a new insight | Founder |
| Fri | Engage with OpenClaw discourse — reply to complaints with helpful positioning (not pitchy) | Both |

### Ongoing rules

- **Reply to every comment** on the threads within 2 hours
- **Quote-tweet** anyone who shares their OpenClaw frustrations (with empathy, not a sales pitch)
- **Never bash OpenClaw directly** — always: "they proved the demand, we built the product"
- **Link to likeclaw.com** only in the final tweet of threads and in standalone tweets — never in replies (feels spammy)
- **Cross-post Thread 1** to LinkedIn with minor formatting adjustments (longer paragraphs OK there)
- **Time all posts** for 9-11am ET (peak developer Twitter engagement)

---

## Hashtags (use sparingly, 1-2 per standalone tweet, none in threads)

- #buildinpublic
- #AIagents
- #indiehackers
- #startups

---

## Metrics to Track

| Metric | Target (Week 1) | Target (Month 1) |
|--------|-----------------|-------------------|
| Thread 1 impressions | 10K+ | 50K+ |
| Profile visits | 500+ | 2,000+ |
| Link clicks to likeclaw.com | 100+ | 500+ |
| Early access signups from Twitter | 30+ | 150+ |
| Follower growth | +200 | +1,000 |
| Engagement rate (likes+replies+RTs / impressions) | >3% | >2.5% |
