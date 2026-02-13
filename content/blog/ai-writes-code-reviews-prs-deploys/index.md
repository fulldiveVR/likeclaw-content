---
title: "We Let Our AI Write Code, Review PRs, and Deploy Itself"
description: "The story of building a fully autonomous development pipeline where AI writes, reviews, tests, and ships its own improvements."
date: 2026-02-03
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "automation", "ai-agents", "productivity"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["code-review"]
related_blog_posts: ["ai-resolving-its-own-issues", "the-sandbox-bet"]
sections:
  - type: hero
  - type: content
  - type: steps
    heading: "The autonomous development pipeline"
    items:
      - title: "Issue filed"
        description: "A bug is reported or a feature is requested via GitHub Issues. Can come from a user, a team member, or automated monitoring."
      - title: "AI reads and understands"
        description: "Claude reads the issue, explores the codebase, identifies the relevant files, and formulates a solution approach."
      - title: "Code is written"
        description: "Claude writes the fix or feature on a new branch. It runs the test suite. If tests fail, it fixes the code and retries."
      - title: "PR is created and reviewed"
        description: "An automated PR is created with a concise summary. A separate Claude instance reviews the code for bugs, security, and style."
      - title: "Human approves"
        description: "A human reviews the PR, the AI's code review comments, and the test results. Then merges or requests changes."
  - type: before_after
    before:
      summary: "Development without AI in the loop"
      items:
        - "Issue sits in backlog for days or weeks"
        - "Developer spends 30+ minutes understanding context"
        - "Code review takes hours of waiting"
        - "Simple bugs consume entire morning blocks"
    after:
      summary: "Development with AI in the loop"
      items:
        - "Issue has a PR within minutes of being filed"
        - "AI has already explored the codebase and written tests"
        - "Code review is instantaneous — human only reviews the review"
        - "Simple bugs are fixed before the team wakes up"
  - type: faq
    heading: "Questions about AI-powered development"
    items:
      - question: "How much of your code is written by AI?"
        answer: "It varies. Routine bug fixes, dependency updates, and simple features are mostly AI-written with human review. Architectural decisions, complex features, and security-sensitive code are human-written with AI review. The ratio shifts week to week."
      - question: "What prevents the AI from making bad changes?"
        answer: "Three layers: automated tests that must pass, AI code review that checks for issues, and mandatory human approval before merge. The AI never pushes directly to main."
      - question: "Can your users do this too?"
        answer: "The same principles apply. LikeClaw users can set up background agents that write code, analyze repositories, and generate reports. The tools we use internally are the same tools we offer to users."
---

## The loop that closed itself

February 3, 2026. The commit message reads: "feat(ci): add closed-loop validation for autonomous Claude in GitHub Actions."

That commit completed a circuit that had been building for weeks. The result: a fully autonomous development loop where AI writes code, tests it, reviews it, creates a PR, and validates the result — all without a human touching the keyboard.

Here's what the loop looks like:

1. An issue is filed on GitHub
2. Claude reads the issue and the codebase
3. Claude writes a fix on a new branch
4. Claude runs the tests
5. If tests fail, Claude reads the errors and fixes the code
6. When tests pass, Claude creates a PR with a summary
7. A separate Claude instance reviews the PR
8. A human reviews everything and decides whether to merge

Steps 1 through 7 happen automatically. Step 8 is the only human intervention.

## How we got here

This didn't happen in one day. It was built incrementally over six weeks, one capability at a time.

**Week 1: Issue resolution (December 25).** We started with the simplest version: Claude reads a GitHub issue, writes a fix, and pushes a branch. No tests. No review. Just "here's a branch with a potential fix, take a look."

**Week 2: PR creation (December 26-27).** Instead of just pushing a branch, Claude creates a proper pull request with a title, description, and linked issue. Now the fix is visible to the team without checking branches manually.

**Week 3: Code review (early February).** A separate Claude workflow triggers on new PRs. It reviews the code for bugs, security issues, and style violations. Comments appear on the PR just like a human reviewer's comments.

**Week 4: Closed-loop validation (February 3).** The final piece: Claude runs the tests before submitting the PR. If tests fail, it reads the error output, modifies the code, and tries again. The PR only gets created when the test suite passes.

Each week added one layer. Each layer made the whole system more reliable.

## What we learned about AI-powered development

**The AI needs constraints, not freedom.** Early on, Claude would sometimes "fix" a minor UI bug by refactoring three modules and changing the database schema. We learned to add explicit constraints: "Only modify files directly related to the issue. Do not refactor. Do not add features. Fix the bug."

**Concise summaries beat detailed explanations.** Claude's first PR descriptions were 2,000 words long. Nobody read them. We tuned the prompt to require summaries under 200 words. "What changed and why" in two sentences. That's all a reviewer needs to start their review.

**The code review catches real problems.** We were skeptical that an AI reviewing AI-generated code would find anything useful. It does. Missing error handling. Potential null references. Unused imports. Security issues. The AI code reviewer isn't perfect, but it catches the 80% of issues that humans catch with a quick scan — and it does it in seconds.

**Separation of concerns matters.** The AI that writes the code and the AI that reviews the code must be separate. Same model, different context, different prompt, different concerns. The writer is optimistic ("here's my solution"). The reviewer is skeptical ("what could go wrong?"). Both perspectives are needed.

## The meta reality

Let's state the obvious: we're building a platform for autonomous AI agents, and we're using autonomous AI agents to build it.

Our users run AI agents that execute code in sandboxed environments, read and write files, and complete tasks autonomously. Our development process runs AI agents that execute code in CI environments, read and write files, and complete tasks autonomously.

The difference is surface-level: our users use LikeClaw's web interface, and our CI uses GitHub Actions. The underlying pattern is identical: define a task, let the AI execute it, review the results.

This isn't a coincidence. We built the development pipeline using the same principles we teach our users. And the things we learn from running this pipeline improve the product we build for them. It's a virtuous cycle.

## The numbers

Since enabling the autonomous development pipeline:

- PRs created by AI: dozens
- Average time from issue to PR: minutes, not hours
- Test failures caught before submission: multiple per week
- Production incidents caused by AI-written code: zero (so far)

That last number is the one that matters most. Zero production incidents. Every AI-written change went through tests, AI review, and human review before merging. The three-layer safety net works.

## This is just the beginning

Today, the AI handles bug fixes, dependency updates, and straightforward feature implementations. Tomorrow, it will handle more complex tasks: multi-file refactoring, performance optimization, test generation.

The key insight isn't that AI can write code. It's that AI can participate in a development workflow with proper guardrails. Tests, reviews, and human oversight make AI-generated code safe. Remove any of those layers and you have a risk. Keep all three and you have a tool that multiplies your team's output.

We're a small team shipping 7.5 commits per day. Some of those commits are human-written. Some are AI-written. All of them are human-approved.

That's the future of software development. Not AI replacing developers. AI accelerating developers. With proper guardrails. At 3 AM. While the team sleeps.
