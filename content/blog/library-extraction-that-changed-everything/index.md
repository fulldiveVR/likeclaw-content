---
title: "The Library Extraction That Changed Everything"
description: "How pulling our chat UI and file system into reusable packages turned a single product into a platform."
date: 2026-02-10
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "architecture", "startup"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["first-commit-to-live-in-48-hours", "from-chat-to-agent-platform"]
sections:
  - type: hero
  - type: content
  - type: steps
    heading: "How we extracted three libraries in one week"
    items:
      - title: "Identify the boundaries"
        description: "Chat rendering, file management, and core utilities had clear interfaces. Everything behind those interfaces could move to packages."
      - title: "Extract and publish"
        description: "We moved chat-ui, vfs-ui, and core-ui-utils to separate packages on GitHub Packages. Same code, properly scoped."
      - title: "Consume our own packages"
        description: "The dashboard switched from local code to published packages. If it broke for us, it would break for anyone."
      - title: "Iterate at package speed"
        description: "Now improvements to chat-ui benefit every product that uses it. One fix, everywhere."
  - type: faq
    heading: "Questions about library extraction"
    items:
      - question: "Isn't it too early to extract libraries in week one?"
        answer: "It depends. If the boundaries are clear — and with chat UI and file management, they were — early extraction prevents entanglement. It's much harder to extract a library from code that has been growing together for six months."
      - question: "How do you manage versioning across packages?"
        answer: "Semantic versioning. Breaking changes get a major bump. We update the dashboard frequently — sometimes multiple times per day — so we catch regressions fast."
      - question: "Did this slow down development?"
        answer: "For about two days, yes. After that, it accelerated development significantly. Changes to the UI library automatically improved every product using it."
---

## The moment a product becomes a platform

There's a specific moment in every product's life where it stops being a single application and starts being a platform. For us, that moment was November 26, 2025 — five days after the first commit.

That's when we extracted our chat interface, virtual file system, and core utilities into three separate, reusable packages: `@fulldiveVR/chat-ui`, `@fulldiveVR/vfs-ui`, and `@fulldiveVR/core-ui-utils`.

It sounds like an engineering decision. It was actually a business decision.

## Why we did it on day five, not day fifty

The conventional wisdom says: don't extract libraries too early. Wait until you have a second use case. Wait until the API stabilizes. Wait until you "know what you're building."

We ignored all of that.

Here's why: we knew we'd have multiple products using the same chat interface. We knew the file management UI would be needed in different contexts. And we knew that the longer we waited, the more tightly these components would be coupled to the dashboard's specific needs.

On day five, the chat-ui package was about 2,000 lines of code. Clean. Well-scoped. Easy to extract.

If we'd waited until day fifty, it would have been 10,000 lines with dozens of implicit dependencies on dashboard-specific state, routing, and configuration. Extracting it then would have been a multi-week project instead of a two-day one.

## What we extracted

**chat-ui** — The entire chat rendering system. Message bubbles, streaming responses, file attachments, agent switching, tool call displays. Everything a user sees when they talk to an AI agent.

**vfs-ui** — The virtual file system interface. File trees, folder creation, file previews, drag-and-drop, upload dialogs. Everything a user sees when managing their files.

**core-ui-utils** — Shared utilities. Theme tokens, common hooks, layout primitives. The stuff that both chat-ui and vfs-ui need but neither should own.

Each became a versioned npm package, published to GitHub Packages, consumed by the dashboard like any other dependency.

## The compounding returns

By February 2026, our chat-ui package was at version 2.0.12. That's dozens of releases — each improving the chat experience across every product that uses it.

When we added background task messages to chat-ui, every product got background task messages. When we added collapsible user messages, every product got collapsible user messages. When we fixed a rendering bug, every product got the fix.

This is the compounding return of early extraction: improvements multiply.

But it goes beyond code reuse. Extracting these libraries forced us to think about our interfaces. What does a chat component need to know? What does a file manager need from its host application? These questions, asked early, produced cleaner answers than they would have months later when everything was tangled together.

## The unexpected benefit: speed

Here's what surprised us most. After the initial extraction cost (about two days of refactoring), our development speed increased.

Why? Because the boundaries were clear. Working on the chat experience meant working in chat-ui. Working on file management meant working in vfs-ui. There was no "I changed the chat and it broke the file manager" because they were literally separate packages with defined interfaces.

New team members could work on chat-ui without understanding the entire dashboard codebase. Bug reports could be immediately triaged to the right package. Testing was faster because each package had its own test suite.

## The lesson for other builders

If you can draw a box around a component — if it has clear inputs, clear outputs, and a clear purpose — extract it early. Don't wait for the mythical "right time." The right time is when the extraction is small and cheap. That window closes faster than you think.

We extracted three libraries in week one. Eighty days later, they've been updated over a hundred times. Every update made every product better. That's the kind of leverage that turns a small team into a productive one.
