---
title: "We Built Billing Before We Built Features"
description: "Why we wired up subscriptions, payment guards, and usage tracking on day three — before most of our features existed."
date: 2026-02-12
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "startup", "pricing", "monetization"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["first-commit-to-live-in-48-hours", "632-commits-in-84-days"]
sections:
  - type: hero
  - type: content
  - type: before_after
    before:
      summary: "The typical startup approach"
      items:
        - "Build the product for 6 months"
        - "Add a 'pricing page' at the last minute"
        - "Discover billing integration takes 3 more weeks"
        - "Ship free forever because billing is 'almost ready'"
    after:
      summary: "What we did instead"
      items:
        - "Billing sync on day three"
        - "Subscription guards from the start"
        - "Free tier with real limits, not infinite runway"
        - "Every new feature inherits billing awareness automatically"
  - type: faq
    heading: "Questions about billing-first development"
    items:
      - question: "Doesn't this slow down early development?"
        answer: "It costs about one day upfront and saves weeks later. Every feature you build after billing is set up automatically respects usage limits. Without it, you build features that work only in a free-forever world, then have to retrofit everything."
      - question: "What about getting early users with a free product?"
        answer: "We have a free tier. Always will. But there's a difference between 'free tier with clear limits' and 'everything is free because we haven't built billing yet.' The first is a strategy. The second is procrastination."
      - question: "What billing system did you use?"
        answer: "We sync subscriptions via RabbitMQ from our central billing service. The dashboard doesn't handle payments directly — it receives subscription status updates and enforces access rules. Clean separation."
---

## The most unpopular opinion in startups

Here's something you won't hear at a startup meetup: we wired up billing on day three.

Not the pricing page. Not the "we'll figure out monetization later" hand-wave. Actual subscription syncing, payment guards, and usage tracking. Before we had half our features built.

Every mentor, every blog post, every Y Combinator video says the same thing: *don't worry about monetization yet. Just get users. Revenue can come later.*

We respectfully disagree.

## Why billing first is actually user-first

The argument against early billing is that it "distracts from building." But here's what actually happens when you defer billing:

You build an AI platform where every user gets unlimited access. You acquire users who love the unlimited access. Then one day you flip the switch and tell those users they need to pay. Some will. Most won't. And the ones who stay are the ones who happened to be using features that fit within your hastily designed pricing tiers.

We didn't want that future.

By building billing on day three, every feature we added after that point was designed with awareness of what tier it belonged to. "Should this be in the free tier or pro?" became a natural question during development, not a painful retrofit six months later.

## What day three looked like

November 24, 2025. Three days after the first commit. The product had chat, file management, workspaces, and basic agent capabilities. Here's what we added:

**Subscription syncing via RabbitMQ.** Our billing service sends subscription status updates. The dashboard receives them and knows exactly what plan each user is on. Real-time. No polling. No stale data.

**Billing guards on protected routes.** Try to access a pro feature without a pro subscription? You get a clean modal explaining the limit and how to upgrade. Not a crash. Not a blank page. A designed experience.

**Credit tracking.** We track AI usage per user. Not because we want to nickle-and-dime people, but because predictable costs require predictable usage tracking. OpenClaw users report spending $50-750/month with zero visibility into where the money goes. We decided that would never be our story.

**Annual subscription handling.** Because we knew some users would want to pay annually, and adding that "later" always means adding it badly.

## The compounding benefit

Here's what most people miss about billing-first: it compounds.

When we added image generation two weeks later, the billing guard was already there. We just tagged image generation as a pro feature and it worked. No additional billing code.

When we added the skills marketplace, same thing. Free users see a "Pro" badge on premium skills. No new billing logic needed.

When we added background task execution, the sandbox execution counter was already tracking usage. We just set the limits per tier.

Every feature we've built in the last 80 days inherited billing awareness for free. That's the compounding benefit of building the foundation early.

## The real cost of "later"

We've watched other startups in our space struggle with this. They build beautiful products with unlimited everything. Then they try to add billing and discover:

- Their database doesn't track usage per user
- Their API doesn't distinguish between free and paid operations
- Their frontend has no concept of "you can't do this on your plan"
- Their users feel betrayed when limits appear

Retrofitting billing into a product that was designed without it is one of the most expensive things a startup can do. Not in money — in architectural debt and user trust.

## Pay as you go

Our pricing ended up simple: pay per task. Every task costs between $0.001 and $0.10 depending on the model. You see the cost before every run. The billing code that enforces this was written on day three and has been running ever since.

Every user knows exactly what they are paying for. Nobody gets a surprise bill.

That's not because we're generous. It's because we built billing before we built features.
