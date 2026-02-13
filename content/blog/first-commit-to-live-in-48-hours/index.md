---
title: "From First Commit to Live Product in 48 Hours"
description: "How we went from an empty repo to a deployed AI agent platform with chat, file management, and workspaces in two days."
date: 2026-02-13
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "startup", "speed"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["email-automation"]
related_blog_posts: ["632-commits-in-84-days", "from-chat-to-agent-platform"]
sections:
  - type: hero
  - type: metrics
    headline: "48 hours from zero to live"
    items:
      - label: "Hours to first deploy"
        value: "48"
      - label: "Features shipped day one"
        value: "12"
      - label: "Lines of boilerplate"
        value: "0"
  - type: content
  - type: faq
    heading: "Questions about building fast"
    items:
      - question: "Did you cut corners to ship that fast?"
        answer: "No. We chose a proven stack (NestJS + React + MongoDB) and focused on decisions that wouldn't need to be reversed. The architecture we built on day one is still running in production today."
      - question: "How did you avoid the rewrite trap?"
        answer: "By building the right abstractions early. Chat, file management, and workspaces were designed as separate modules from the start. We've added 600+ commits since and never had to rewrite a core module."
      - question: "What's the one thing you'd do differently?"
        answer: "We'd add end-to-end tests earlier. We added them on day three, which was fine, but having them from hour one would have saved a few debugging sessions."
---

## November 21, 2025, 9:14 AM

That's when we pushed the first commit. An empty project. A blank canvas. By November 23rd at midnight, we had a live product with a custom domain, serving real users.

This isn't a story about cutting corners or shipping broken software. It's about what happens when you know exactly what you're building and refuse to waste time on anything else.

## What shipped in 48 hours

Here's what was live by end of day two:

**A real-time AI chat interface.** Not a wrapper around an API. A proper chat system with session management, message history, and streaming responses. Users could have conversations with AI agents that actually remembered context.

**A virtual file system.** Users could create folders, upload files, rename them, organize them into workspaces. The AI could read and write to these files during conversations. Not a toy demo — a real file system backed by MongoDB.

**Workspaces with agent switching.** Different workspaces could use different AI agents with different capabilities. A user could have a coding workspace, a writing workspace, and a research workspace — each with its own context and files.

**User authentication and sync.** Connected to our auth system via RabbitMQ. Users logged in and their data was there. Across devices. Immediately.

**Image generation.** The AI could generate images during conversations. Not just text responses — actual visual output.

**Templates.** Pre-built starting points so users didn't face a blank screen on their first visit.

**Deployment pipeline.** Dockerized, deployed, running on a custom domain with proper environment configuration.

## The decisions that made it possible

Speed like this doesn't come from working 48 hours straight (though there was plenty of that). It comes from the decisions you make before you write the first line of code.

**Decision 1: MongoDB over Mongoose.** We started with Mongoose for about four hours. Then switched to raw MongoDB drivers. Mongoose adds a schema validation layer that's helpful for large teams but pure overhead for a small team that knows its data model. Four hours "wasted" that saved us dozens of hours in the weeks that followed.

**Decision 2: Build the server and client in one repo.** Monorepo. One `docker-compose.yml`. One deploy command. No cross-repo coordination. No "the API is deployed but the frontend isn't." When you're moving fast, reducing the number of things that can go out of sync is more important than organizational purity.

**Decision 3: Ship to production on day two, not day twenty.** We deployed before we were "ready." The domain was configured, SSL was set up, environment variables were in place — all before half the features were built. Why? Because deploying is the part that surprises you. Better to discover those surprises on day two with three features than on day twenty with thirty.

## What we didn't build

Just as important as what we shipped is what we deliberately left out:

- No admin panel. We used MongoDB Compass directly.
- No custom design system. We used clean defaults and iterated later.
- No analytics. We watched server logs.
- No automated testing. (That came on day three.)
- No documentation. The code was the documentation.

Each of these would have been the "responsible" thing to build. Each would have cost us a day. And none of them would have taught us what we learned by putting the product in front of real users on day two.

## The lesson

There's a version of this story where we spend two weeks on architecture diagrams. Where we debate database schemas in a Google Doc. Where we set up a proper CI/CD pipeline before writing any application code.

That version of the story ends with a beautiful plan and no product.

The version that actually happened ended with a working product and a long list of things to improve. We'll take that trade every time.

Forty-eight hours. First commit to live product. Not because we're geniuses. Because we made decisions fast, shipped faster, and fixed things in production like everyone actually does — but few admit.

The product you see today, 84 days and 632 commits later, started right there. In 48 hours.
