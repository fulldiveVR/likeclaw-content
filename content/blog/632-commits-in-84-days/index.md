---
title: "632 Commits in 84 Days: What We Learned Shipping Every Day"
description: "The cadence, the chaos, and the compound effects of relentless daily shipping."
date: 2026-02-05
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "startup", "productivity"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["first-commit-to-live-in-48-hours", "from-chat-to-agent-platform"]
sections:
  - type: hero
  - type: metrics
    headline: "84 days of shipping"
    items:
      - label: "Total commits"
        value: "632"
      - label: "Average per day"
        value: "7.5"
      - label: "Longest streak"
        value: "84 days"
      - label: "Days with zero commits"
        value: "0"
  - type: content
  - type: steps
    heading: "What 84 days of daily shipping looks like"
    items:
      - title: "Week 1-2: Foundation sprint"
        description: "Chat, files, workspaces, billing, internationalization, deployment. The core product materialized in 14 days."
      - title: "Week 3-4: Feature explosion"
        description: "Scheduling, onboarding, localization, code execution tools. The product went from 'it works' to 'it's useful.'"
      - title: "Week 5-8: Platform maturity"
        description: "AI studio, image generation, skills marketplace, model selection. The product became a platform."
      - title: "Week 9-12: The sandbox era"
        description: "E2B integration, background agents, eval framework, CI/CD automation. The platform became autonomous."
  - type: faq
    heading: "Questions about shipping speed"
    items:
      - question: "How do you maintain quality while shipping this fast?"
        answer: "Automated tests, code review (both human and AI), and sandboxed execution that limits blast radius. We also ship to staging first and promote to production after verification."
      - question: "How big is the team?"
        answer: "Small. We won't share exact numbers, but think single digits. The tools we use — AI-assisted development, reusable libraries, automated testing — multiply our output significantly."
      - question: "Don't you accumulate technical debt at this speed?"
        answer: "Some, yes. But we address it continuously, not in big 'tech debt sprints.' Every week includes refactoring alongside new features. The key is that our architecture absorbs change well — adding a feature rarely requires modifying existing ones."
      - question: "What's your deploy process?"
        answer: "Push to main, automated build, Docker container, deploy to staging. After verification, promote to production. The whole cycle takes about 15 minutes."
---

## The number that tells the story

632 commits. 84 days. Zero days without a commit.

From November 21, 2025 to February 13, 2026, we shipped code every single day. Weekdays. Weekends. Holidays. Christmas. New Year's. Every day.

This isn't about hustle culture or grinding. It's about what happens when you maintain momentum on a product that's growing faster than you planned.

## The daily shipping rhythm

Here's what 7.5 commits per day actually looks like:

**Morning:** Review what shipped overnight (remember, the AI resolves issues at 3 AM). Check staging. Identify what's next.

**Mid-day:** Ship the main feature of the day. This is usually a PR with 3-5 commits: the feature, a fix discovered during development, and a version bump.

**Evening:** Polish, fix edge cases, update dependencies. The commits that aren't glamorous but keep the product running smoothly.

Some days had one commit. Some days had twenty. November 22nd — day two — had twelve commits. The day we integrated E2B sandboxes had over a dozen. The pattern varies, but the streak never broke.

## What compound shipping looks like

The most interesting thing about shipping every day isn't any individual commit. It's the compound effect.

**Week 1:** Chat interface + file system + workspaces. A functional product.

**Week 2:** Billing + internationalization + UI libraries. A sustainable product.

**Week 4:** Scheduling + onboarding + code execution. A useful product.

**Week 8:** Image generation + skills + model selection. A platform.

**Week 12:** Sandboxed execution + background agents + autonomous CI. An autonomous platform.

Each week builds on the last. Features don't exist in isolation — they combine. Scheduling + sandboxes = background task execution. Billing + image generation = sustainable creative tools. Skills + sandboxes = safe automation marketplace.

The compound effect means that week 12's output is qualitatively different from week 1's, not just quantitatively larger. We're not just building more features. We're building more capable combinations of features.

## The commits that matter most

If you scroll through our git history, you'll find three types of commits:

**The builders.** "feat: add sandbox agents module," "feat: add workspace settings panel," "feat: add skills system with ClawHub import." These are the big features. They get the blog posts. They show up in changelogs.

**The fixers.** "fix: prevent infinite message polling loop," "fix: cascade delete events on session deletion," "fix: embed image URLs in markdown to prevent LLM URL corruption." These are less glamorous but arguably more important. Each one represents a real user hitting a real problem.

**The invisible upgrades.** "chore: bump @fulldiveVR/chat-ui to 2.0.12," "refactor: route all judge calls through OpenRouter," "perf: add PERF tracing logs." These don't change what users see, but they change how well it works. Performance improvements. Security patches. Dependency updates.

The ratio is roughly 30% builders, 40% fixers, 30% invisible. That ratio feels healthy. Too many builders and not enough fixers means growing bugs. Too many fixers and not enough builders means stagnation. Too few invisible commits means accumulating debt.

## The holidays

November 28 (Thanksgiving): 14 commits. Template improvements, UI library fixes, agent modernization.

December 25 (Christmas): 6 commits. Auto issue resolver, subscription protection, workflow automation.

January 1 (New Year's): 8 commits. Favicon fixes, session improvements, file sharing.

We're not bragging about working on holidays. Some of these were scheduled merges. Some were the AI fixing things autonomously. Some were a founder who couldn't stop thinking about a bug.

The point isn't "we worked on Christmas." The point is "the product improved on Christmas." Whether that improvement came from a human or an AI, the users don't care. They just see a better product when they open it next.

## What we learned

**Ship the smallest meaningful unit.** Not the whole feature. The smallest thing that makes the product better. A button that works. An error that's handled. A label that's clearer. Small commits are easy to review, easy to revert, and easy to understand.

**Fix bugs the day they're found.** Our average time from bug report to fix is measured in hours, not days. This is only possible because we ship every day. A team that ships weekly holds bugs for a week. A team that ships daily fixes them today.

**Let the streak motivate you.** There's something psychological about a daily streak. Once you've shipped for 30 days straight, you don't want to break it on day 31. The streak becomes its own motivation. It's not sustainable forever — and we'll take breaks — but for a launch phase, it's powerful.

**Compounding is real.** Day 84's commit is qualitatively different from day 1's commit. Not because we're smarter. Because we're building on 83 days of foundation. Every day makes the next day more productive. That's the real power of daily shipping.

632 commits. 84 days. One product that went from nothing to autonomous AI agent platform.

The next 84 days will be even better.
