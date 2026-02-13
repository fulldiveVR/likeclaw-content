---
title: "Teaching Our AI to Schedule Itself"
description: "How we built autonomous task scheduling so your AI agent works while you sleep."
date: 2026-02-09
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "automation", "ai-agents"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["email-automation"]
related_blog_posts: ["from-chat-to-agent-platform", "the-sandbox-bet"]
sections:
  - type: hero
  - type: metrics
    headline: "Autonomous scheduling, built in a week"
    items:
      - label: "Days to build scheduling"
        value: "5"
      - label: "Lines of scheduling code"
        value: "~800"
      - label: "Agents running on schedule"
        value: "24/7"
  - type: content
  - type: before_after
    before:
      summary: "AI assistants before scheduling"
      items:
        - "You ask a question, you get an answer"
        - "Close the tab, the AI stops"
        - "Want daily reports? Set a reminder to ask daily"
        - "Background work means keeping a browser tab open"
    after:
      summary: "AI agents with scheduling"
      items:
        - "Define a task, set a schedule, walk away"
        - "Agent runs at 6 AM whether you're awake or not"
        - "Daily reports generated and waiting in your inbox"
        - "Background execution in cloud sandboxes"
  - type: faq
    heading: "Questions about AI scheduling"
    items:
      - question: "What kinds of tasks can be scheduled?"
        answer: "Anything an AI agent can do in a single session: generate reports, analyze data, check websites, process files, run code. If you can describe it in a prompt, you can schedule it."
      - question: "What happens if a scheduled task fails?"
        answer: "You get a notification in your inbox with the error details. Failed tasks don't retry automatically — you can review what went wrong and rerun manually or adjust the schedule."
      - question: "Can I schedule tasks across different workspaces?"
        answer: "Yes. Each workspace can have its own scheduled tasks with its own agents and files. A marketing workspace might have a daily content analysis, while a development workspace has a weekly code review."
---

## The question that changed our roadmap

Two weeks into building LikeClaw, a beta user asked a simple question: "Can it run this every morning at 6 AM?"

They had an AI agent that analyzed their inbox and created a summary. It worked perfectly when they manually triggered it. But they wanted it to run automatically before their morning coffee. Every day. Without them touching anything.

We didn't have an answer. So we built one.

## What "scheduling" actually means for an AI agent

When we say "schedule," we don't mean a cron job that pings an API. We mean: the AI agent wakes up at the specified time, loads the workspace context, reads the relevant files, executes the task with full tool access, saves the results, and sends you a notification that it's done.

The user doesn't need to be online. Doesn't need a browser tab open. Doesn't even need to be awake. The agent runs in the cloud, in its own sandbox, on its own schedule.

This is the line between a chatbot and an agent. A chatbot answers when you ask. An agent acts on your behalf, on your schedule, whether you're watching or not.

## How we built it

The scheduling system went from first commit to production in five days. Here's the journey:

**Day one: The scheduler module.** We added a scheduling service that could register tasks with cron-style timing. Every minute, it checks: are there tasks that need to run? If yes, trigger them.

**Day two: The UI.** Users needed to create and manage schedules without writing cron expressions. We built a clean interface: pick a task, pick a time, pick a frequency. Daily, weekly, custom. Done.

**Day three: Events and notifications.** When a scheduled task completes, the user needs to know. We wired up a notification system — events that appear in your inbox with the task results. "Your daily report is ready" at 6:05 AM, waiting for you.

**Day four: Session management.** A scheduled task creates a new session in the workspace. It runs, produces output, and the session is preserved so you can review exactly what the agent did and why.

**Day five: Edge cases.** What if a task is still running when the next scheduled run triggers? What if the user deletes the workspace? What if the agent hits an error mid-task? We handled each case with clear rules: don't double-run, clean up orphaned schedules, surface errors to the user.

## The surprise: scheduling changed how people use the product

We expected scheduling to be a nice-to-have. A "power user" feature that 5% of users would discover and the rest would ignore.

We were wrong.

Scheduling changed the mental model. Users stopped thinking of LikeClaw as "a chat app for AI." They started thinking of it as "my AI assistant that's always working."

One user set up a daily competitive analysis: every morning at 7 AM, the agent checks competitor websites, summarizes changes, and drops a report in their workspace. They never run it manually anymore. It just appears.

Another user scheduled weekly code reviews. Every Friday at 4 PM, the agent reviews the week's commits, identifies potential issues, and generates a summary. The developer reads it Monday morning with their coffee.

The pattern is always the same: define once, run forever. That's the promise of autonomous agents. Scheduling is how you deliver on it.

## From "chat with AI" to "AI that works for you"

There's a fundamental difference between software you use and software that works on your behalf. Email is software you use. A spam filter is software that works on your behalf.

Scheduling moved LikeClaw from the first category to the second. You're not using the AI. The AI is working for you. On your schedule. With your data. In your workspaces.

That's the future of AI agents. Not smarter chatbots. Autonomous workers that run in the background, complete tasks, and surface results when you need them.

We built that future in five days. And we've been improving it every day since.
