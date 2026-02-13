---
title: "Our AI Resolves Its Own GitHub Issues at 3 AM"
description: "How we set up Claude to automatically fix bugs, create PRs, and review its own code — without a human touching the keyboard."
date: 2026-02-07
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "automation", "ai-agents", "productivity"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["code-review"]
related_blog_posts: ["teaching-ai-to-schedule-itself", "ai-writes-code-reviews-prs-deploys"]
sections:
  - type: hero
  - type: content
  - type: before_after
    before:
      summary: "Traditional bug fixing"
      items:
        - "Developer sees issue in the morning"
        - "Spends 30 min understanding the bug"
        - "Writes a fix, creates a PR"
        - "Waits for code review"
        - "Bug fixed 4-8 hours after discovery"
    after:
      summary: "AI-assisted bug fixing"
      items:
        - "Issue is filed (manually or automatically)"
        - "Claude picks it up within minutes"
        - "Fix is committed, PR is created, code is reviewed"
        - "Human reviews the PR in the morning"
        - "Bug fixed before anyone wakes up"
  - type: faq
    heading: "Questions about autonomous AI development"
    items:
      - question: "Does the AI deploy code to production automatically?"
        answer: "No. The AI creates branches and pull requests. A human always reviews and merges. The AI accelerates the fix-to-PR pipeline, but deployment remains a human decision."
      - question: "How often does the AI get it wrong?"
        answer: "It depends on the complexity. For straightforward bugs with clear error messages, it's surprisingly accurate. For complex architectural issues, it usually identifies the right area but may need human guidance on the approach."
      - question: "Isn't this risky?"
        answer: "Less than you'd think. The AI works on branches, never on main. Every change goes through a PR. The AI even reviews its own code for obvious issues before submitting. And a human always has the final say."
---

## Christmas Day, 2025

Most teams take December 25th off. We did too — sort of. But our AI didn't.

On Christmas Day, we pushed a commit titled "add claude auto issue resolver." It was a GitHub Actions workflow that did something unusual: when a new issue was filed in our repository, Claude would automatically read the issue, analyze the codebase, write a fix, create a branch, and open a pull request.

No human in the loop. The AI reads the bug report. The AI fixes the bug. The AI submits the fix for review.

We came back from the holiday to find pull requests waiting for us. Authored by an AI. At 3 AM.

## Why we built this

We're a small team building a complex platform. At 632 commits in 84 days, we're shipping fast. But speed creates a maintenance challenge: bugs don't wait for business hours.

A user in Shanghai reports an issue at 2 PM their time. That's 1 AM for us. With a traditional workflow, the bug sits untouched for 8 hours until someone wakes up, reads the issue, and starts working on it.

With the auto issue resolver, Claude picks up the issue within minutes. By the time we wake up, there's a pull request waiting with a fix, a description of what was changed and why, and an automated code review.

We're not replacing developers. We're giving them a head start. Instead of "read issue, understand bug, write fix, create PR," the morning workflow becomes "review PR, approve or request changes, merge."

## The evolution: from issue resolver to full CI pipeline

The Christmas Day commit was just the beginning. Over the following weeks, we built out the entire autonomous development pipeline:

**Auto issue resolution.** Claude reads new issues, analyzes the relevant code, writes a fix, and creates a PR. The commit messages reference the issue number. The PR description explains the change.

**Automated code review.** When a PR is created — by a human or by Claude — a separate Claude instance reviews the code. It checks for bugs, security issues, style violations, and test coverage. The review appears as PR comments, just like a human reviewer's.

**Closed-loop validation.** Claude doesn't just write code. It runs the tests. If the tests fail, it reads the error, fixes the code, and tries again. The PR only gets submitted when the tests pass.

**PR auto-creation.** When Claude pushes a branch, it automatically creates a PR with a summary of changes. No manual step required.

## The meta moment

There's something deeply satisfying about an AI platform that uses AI to build itself.

Our product lets users run AI agents that execute code, manage files, and automate tasks. And our development process uses AI agents that execute code, manage files, and automate tasks.

We eat our own cooking. Every day.

When Claude resolves an issue in our repository, it's using the same patterns that our users use when they run AI agents on LikeClaw. Sandboxed execution. File system access. Tool calling. The difference is that our user-facing agents run in E2B sandboxes in the cloud, while our CI agent runs in GitHub Actions.

Same principles. Same capabilities. Same trust model: AI does the work, humans review the results.

## What we learned

**Concise PR summaries matter.** Early on, Claude would write 2,000-word PR descriptions for a three-line fix. We tuned the prompts to enforce concise summaries. "What changed and why" in two sentences, not two pages.

**The AI needs constraints.** Without guardrails, Claude would sometimes "fix" an issue by refactoring half the codebase. We added rules: only change files directly related to the issue. Don't refactor. Don't add features. Fix the bug.

**Code review catches real issues.** The automated code review has caught actual bugs — null pointer risks, missing error handling, potential security issues. It's not a replacement for human review, but it's a meaningful first pass.

**The 3 AM bug fix is real.** We've woken up to pull requests that fixed issues reported overnight. Reviewed the change. Merged it. The bug was fixed before our morning coffee was cold. That's the future of software development.

## This is what AI agents are for

Not generating lorem ipsum. Not writing cover letters. Not summarizing articles you could read yourself.

AI agents are for doing real work, autonomously, at scale, around the clock. Fixing bugs while the team sleeps. Reviewing code before the author finishes lunch. Creating pull requests from issue descriptions without a human typing a single line.

We built this for ourselves first. Now we're building it for everyone.
