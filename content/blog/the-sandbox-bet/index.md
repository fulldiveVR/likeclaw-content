---
title: "The Sandbox Bet"
description: "How we bet the product on E2B sandboxed execution — and why it was the most important decision we made."
date: 2026-02-06
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "security", "ai-agents", "sandbox"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["skills-marketplace-without-malware", "from-chat-to-agent-platform"]
sections:
  - type: hero
  - type: metrics
    headline: "Security by architecture, not by hope"
    items:
      - label: "Malicious skills on our marketplace"
        value: "0"
      - label: "User systems compromised"
        value: "0"
      - label: "Sandbox spin-up time"
        value: "<2s"
  - type: content
  - type: comparison_table
    heading: "Sandbox vs. raw system access"
    columns:
      - name: "LikeClaw (E2B Sandbox)"
        highlight: true
      - name: "Local AI agents"
        highlight: false
    rows:
      - label: "Code execution environment"
        values: ["Isolated cloud container", "Your actual machine"]
        highlights: ["brand", "error"]
      - label: "File system access"
        values: ["Workspace files only", "Every file on your system"]
        highlights: ["brand", "error"]
      - label: "API key storage"
        values: ["Encrypted, per-sandbox", "Plaintext in config files"]
        highlights: ["brand", "error"]
      - label: "After task completes"
        values: ["Sandbox destroyed", "Everything persists"]
        highlights: ["brand", "default"]
      - label: "Malicious code risk"
        values: ["Contained to sandbox", "Full system compromise"]
        highlights: ["brand", "error"]
    footer: "Sandboxed execution means a mistake stays contained."
  - type: faq
    heading: "Questions about sandboxed execution"
    items:
      - question: "What is E2B exactly?"
        answer: "E2B (Environment to Build) provides cloud-based sandboxed environments for AI agents. Each sandbox is an isolated container with its own file system, network, and process space. Code runs inside the sandbox and can't affect anything outside it."
      - question: "Does sandboxing limit what the AI can do?"
        answer: "Inside the sandbox, the AI has full capabilities: file system access, code execution, network requests, package installation. The difference is that 'full capabilities' applies to the sandbox environment, not your actual machine."
      - question: "What happens to my data in the sandbox?"
        answer: "Files you upload are available inside the sandbox. Files the AI creates are synced back to your workspace. When the task completes, the sandbox is destroyed. Your workspace files persist in our encrypted storage."
---

## January 25, 2026: the bet

Two months into building LikeClaw, we made the decision that would define the product. We bet everything on E2B sandboxed execution.

Until that point, our AI agents ran tasks in a relatively traditional way. After that point, every task — every code execution, every file operation, every background job — ran inside an isolated E2B sandbox container.

This wasn't a security feature we bolted on. It was a fundamental architectural decision that changed how the entire platform worked. And it was the best decision we've made.

## Why sandboxing matters more than anything else

Look at the AI agent landscape in early 2026. One pattern repeats everywhere: users giving AI agents unrestricted access to their machines.

OpenClaw runs on your local system. It reads your files. It executes code with your permissions. It stores API keys in plaintext. Security researchers have documented [widespread vulnerabilities](/blog/openclaw-security-what-you-need-to-know/) in the platform and its marketplace, prompting warnings from multiple security organizations.

The root cause isn't that OpenClaw is badly written. It's that the architecture is fundamentally unsafe. When you give an AI agent raw access to your system, any mistake — by the AI, by a skill author, by a prompt injection attack — has unlimited blast radius. One bad skill can install malware on your machine. One prompt injection can read your SSH keys. One hallucinated command can delete your files.

Sandboxing eliminates the entire category of risk.

## How our sandboxes work

When you run a task on LikeClaw, here's what happens:

**A fresh sandbox is created.** An isolated E2B container spins up in under two seconds. It has its own file system, its own process space, its own network. It is completely isolated from every other sandbox and from every other user.

**Your workspace files are synced in.** The files in your workspace are copied into the sandbox. The AI can read them, modify them, create new ones. But only within the sandbox.

**The AI executes the task.** Inside the sandbox, the AI has full capabilities. It can run code, install packages, make network requests, read and write files. It's a fully functional environment. The difference is that "fully functional" means the sandbox, not your machine.

**Results are synced back.** When the task completes, the files the AI created or modified are synced back to your workspace in our encrypted storage.

**The sandbox is destroyed.** Gone. Every process killed. Every file deleted. Every network connection closed. Nothing persists. Nothing leaks. Nothing lingers.

If the AI does something wrong — runs malicious code, follows a prompt injection, executes a bad skill — the damage is contained to a sandbox that will be destroyed in seconds. Your machine, your files, your API keys, your credentials are never at risk.

## The engineering challenge

Sandboxing sounds simple. "Just run it in a container." In practice, it was the most complex engineering challenge of the entire project.

**File synchronization.** Users need their files inside the sandbox, and they need the AI's output back in their workspace. This bi-directional sync needs to be fast, reliable, and handle conflicts. We built a VFS (Virtual File System) sync layer that watches for changes in both directions.

**Background task execution.** Scheduled tasks run in sandboxes too. A task that runs at 3 AM needs to spin up a sandbox, sync files, execute, sync results back, and clean up — all without a user being online.

**Performance.** Sandbox creation adds latency. We optimized spin-up time to under two seconds. Users barely notice. But getting there required careful template management, lazy initialization, and pre-warming strategies.

**Cost.** Every sandbox costs compute resources. We had to balance security (always sandbox) with economics (sandboxes cost money). The answer was per-tier sandbox limits — free users get a set number of executions, pro users get more, power users get unlimited.

## The line in the sand

Here's the thing about security: you can't half-do it.

You can't sandbox some tasks and not others. You can't sandbox free users but let paid users run raw. You can't sandbox code execution but not file access. Any gap in the sandbox model becomes an attack vector.

So we drew a line: everything runs in a sandbox. No exceptions. No escape hatches. No "expert mode" that bypasses isolation.

This means some things are slightly slower than running locally. This means some things require an extra step (syncing files in and out). This means we can't offer the "full machine access" that local AI agents provide.

We're fine with that. Because we also can't offer malware installation, credential theft, or system compromise. And neither can our users.

0 malicious skills. 0 compromised systems. 0 security incidents.

That's the sandbox bet. And it's paying off.
