---
title: "OpenClaw Security Issues: What You Need to Know in 2026"
description: "A factual guide to OpenClaw security risks, what researchers found, and how to protect yourself."
date: 2026-02-12
draft: false
tags: ["security", "openclaw", "ai-agents"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["code-execution"]
related_blog_posts: ["sandboxed-ai-agents-future", "migrating-from-openclaw", "ai-skills-marketplace-security"]
sections:
  - type: hero
  - type: metrics
    headline: "The security numbers"
    items:
      - label: "Malicious skills found on ClawHub"
        value: "341+"
        source: "Snyk Research, 2026"
      - label: "Skills with prompt injection"
        value: "36%"
        source: "Snyk ToxicSkills Report"
      - label: "Packages installing macOS stealer"
        value: "335"
        source: "Atomic Stealer / AMOS"
      - label: "Security orgs issuing warnings"
        value: "5"
        source: "Kaspersky, Cisco, Snyk, Wiz, Bitsight"
  - type: content
  - type: cards
    heading: "The five security risks"
    items:
      - icon: "1"
        title: "Supply Chain Attacks"
        description: "341+ malicious skills on ClawHub. 335 used fake prerequisites to install macOS stealer malware. No adequate vetting or code review for submissions."
      - icon: "2"
        title: "Raw System Access"
        description: "Full filesystem, shell, and network access with only a weak allowlist standing between the agent and your entire machine."
      - icon: "3"
        title: "Credential Exposure"
        description: "API keys stored in plaintext at ~/.clawdbot. Deleted keys persist in .bak files. One breach exposes every connected service."
      - icon: "4"
        title: "Remote Code Execution"
        description: "A documented one-click RCE vulnerability allows attackers to execute arbitrary code on your machine through crafted skill packages."
      - icon: "5"
        title: "Data Exfiltration"
        description: "Cisco demonstrated that a third-party skill can silently extract sensitive data from your system and send it to an external server."
  - type: text
    heading: "There's a better approach"
    paragraphs:
      - "These five risks share a common root cause: the agent runs directly on your machine with broad system access. Every skill, every command, every LLM response executes in your environment with your permissions."
      - "Sandboxed execution is the architectural answer. When code runs in an isolated container that is created for each task and destroyed after, supply chain attacks have nothing to steal. Credentials never touch the execution environment. Exfiltrated data goes nowhere. The blast radius of any vulnerability shrinks from your entire system to an empty, ephemeral sandbox."
    tagline: "Security is not a feature you bolt on. It is an architecture you build from."
  - type: steps
    heading: "How sandboxed AI agents solve these problems"
    items:
      - title: "Supply chain attacks are contained"
        description: "Skills execute in isolated containers with no access to your host filesystem, credentials, or network. A malicious skill can only damage an empty sandbox that gets destroyed seconds later."
      - title: "System access is eliminated by design"
        description: "There is no host machine to access. The agent runs in the cloud inside an E2B container. Your laptop, your files, your shell history -- none of it is reachable."
      - title: "Credentials are encrypted and separated"
        description: "API keys are stored in encrypted vaults, never in plaintext config files. The execution environment receives only the tokens it needs for each specific task, scoped and time-limited."
      - title: "Remote code execution has no target"
        description: "Even if an attacker achieves code execution, they land inside a throwaway container with no persistent data, no credentials, and no network route back to your machine."
      - title: "Data exfiltration hits a dead end"
        description: "Sandboxed containers have controlled network policies. Outbound connections to unknown endpoints are blocked. Your data stays in your workspace, not in the skill's execution context."
  - type: faq
    heading: "Common questions about OpenClaw security"
    items:
      - question: "Is OpenClaw safe to use?"
        answer: "It depends on your threat model. OpenClaw gives agents full access to your filesystem, shell, and network. Five security organizations (Kaspersky, Cisco, Snyk, Wiz, and Bitsight) have published warnings about specific vulnerabilities. If you do use it, avoid installing third-party skills from ClawHub without reviewing their source code, and never store API keys in the default plaintext location."
      - question: "What are the alternatives to OpenClaw?"
        answer: "You have several options. For sandboxed cloud-based AI agents, LikeClaw runs all code in isolated E2B containers with vetted skills and encrypted credentials. For minimal local setups, NanoClaw is a 700-line fork that runs inside Apple containers. For chat-only AI (no code execution), Claude, ChatGPT, and Gemini are safer but less capable. Your choice depends on whether you need autonomous code execution and how much setup you are willing to manage."
      - question: "Can I secure OpenClaw myself?"
        answer: "Partially. You can self-host on an isolated virtual machine, avoid ClawHub skills entirely, move API keys out of ~/.clawdbot into a proper secrets manager, and run it behind a firewall. The community openclaw-secure-stack project adds a skills scanner and prompt injection protection. But the fundamental issue -- raw system access for every execution -- remains an architectural limitation that cannot be patched away."
      - question: "What about NanoClaw?"
        answer: "NanoClaw is a promising minimal fork. At 700 lines of TypeScript, it runs inside Apple containers for basic isolation and is built on the Anthropic Agents SDK. It solves some security issues but is limited to macOS, supports fewer integrations, and is still early-stage. It is a good option if you want a local-first approach with better security than stock OpenClaw."
      - question: "How does sandboxed execution actually work?"
        answer: "Cloud-based sandboxing uses isolated containers (like E2B) that are created for each task and destroyed after completion. The agent's code runs inside this container, which has its own filesystem, network rules, and resource limits. It cannot see or touch your local machine. Think of it like running code in a clean room that gets incinerated after every use. Your files, credentials, and system remain untouched regardless of what the agent does inside the sandbox."
---

## OpenClaw proved something important

OpenClaw reached 145,000+ GitHub stars in 10 weeks. It is the fastest-growing open-source project in recent memory. And the growth was earned. The idea of an autonomous AI agent that actually does things -- executes code, manages files, runs scripts, monitors your inbox -- resonated with hundreds of thousands of developers.

The vision is right. An AI that talks is useful. An AI that acts is transformative.

But the security model has critical flaws that five major organizations have now documented. This is not speculation. These are findings from Snyk, Kaspersky, Cisco, Wiz, and Bitsight, published in peer-reviewed research and official security advisories. If you use OpenClaw or are considering it, you need to understand what they found.

## The ClawHub supply chain problem

ClawHub is OpenClaw's community marketplace for skills -- pre-built packages that extend what the agent can do. As of February 2026, it hosts 5,705 community-built skills. Anyone with a GitHub account older than one week can publish.

Snyk's ToxicSkills research found that **341 of those skills are malicious**. Of those, 335 use fake prerequisites to install macOS stealer malware, specifically Atomic Stealer (AMOS), which harvests browser passwords, crypto wallets, and session cookies.

Worse: Snyk analyzed a broader sample and found that **36% of ClawHub skills contain prompt injection** -- hidden instructions that hijack the agent's behavior. A skill that claims to format your emails could silently instruct the agent to exfiltrate your files.

This is not a hypothetical. It is a measured, published finding.

## Raw system access with a thin guardrail

OpenClaw runs as a long-lived process on your machine with access to your filesystem, shell, and network. The security model relies on an allowlist -- a list of approved commands the agent can run. Everything else is theoretically blocked by parsing shell AST patterns.

In practice, this is a weak boundary. The allowlist approach means security depends on predicting every dangerous command pattern in advance. Researchers have demonstrated bypasses. The Kaspersky blog documented specific scenarios where the agent's broad permissions allow lateral movement across your system.

The core issue: OpenClaw's security model is **opt-out** (block known-bad patterns) rather than **opt-in** (allow only explicitly approved actions in isolated environments). Opt-out security has a long history of failure in software engineering.

## Credential exposure in plaintext

OpenClaw stores API keys in `~/.clawdbot` in plaintext. Your OpenAI key, Anthropic key, Google key, and any service tokens the agent needs -- all sitting in a readable file on your filesystem.

It gets worse. When users rotate keys, the old values are sometimes preserved in `.bak` files in the same directory. A malicious skill -- or any process with file read access -- can harvest both current and historical credentials in a single read operation.

This is not an edge case. It is the default behavior.

## One-click remote code execution

Security researchers documented a one-click RCE vulnerability in OpenClaw's skill installation flow. A crafted skill package can execute arbitrary code on the host machine during installation -- before the user has a chance to review what it does.

Combined with the ClawHub supply chain problem, this creates a direct attack path: publish a malicious skill, wait for installations, execute code on every machine that installs it.

## Cisco's data exfiltration demonstration

Cisco's AI security team published a detailed demonstration showing how a third-party skill can silently extract sensitive data from the host system. The skill appears benign -- performing its advertised function -- while simultaneously reading files and sending contents to an external server.

Because OpenClaw skills run with the same permissions as the agent (which has broad system access), there is no isolation boundary between what a skill is supposed to do and what it actually does.

## What the security community is saying

The response from the security community has been direct:

- **XDA-Developers** published an article titled "Please stop using OpenClaw"
- **Computerworld** described the platform as "a security nightmare"
- **Gary Marcus** called it "a disaster waiting to happen"
- **Kaspersky** published a detailed blog post cataloging specific vulnerabilities and recommending users isolate OpenClaw on dedicated hardware

These are not fringe voices. They represent the mainstream consensus of the security research community.

## What you can do

If you are currently using OpenClaw, you have three options:

**Option 1: Harden your existing setup.** Move OpenClaw to an isolated virtual machine. Avoid all ClawHub skills. Store API keys in a proper secrets manager instead of `~/.clawdbot`. Use the community [openclaw-secure-stack](https://github.com/openclaw/openclaw-secure-stack) for skills scanning and prompt injection protection. This reduces risk but does not eliminate the fundamental architectural issue.

**Option 2: Try NanoClaw.** This 700-line TypeScript fork runs inside Apple containers, providing meaningful isolation on macOS. It is minimal, supports fewer integrations, and is early-stage -- but it addresses the raw system access problem.

**Option 3: Switch to a sandboxed alternative.** Cloud-based platforms like [LikeClaw](/comparisons/likeclaw-vs-openclaw/) run all agent code inside isolated E2B containers. Skills are vetted before publishing. Credentials are encrypted. There is no host machine to compromise. The tradeoff is that your agent runs in the cloud rather than locally.

The right choice depends on your priorities. If local-first privacy is non-negotiable, harden your setup or try NanoClaw. If security and zero-setup matter more, [sandboxed cloud agents](/blog/sandboxed-ai-agents-future/) eliminate the entire category of risk.

## The deeper lesson

OpenClaw's security problems are not bugs to be patched. They are consequences of an architectural decision: give the agent full system access and figure out security later.

That approach does not scale. As AI agents become more capable and more autonomous, the blast radius of a security failure grows. The industry is moving toward sandboxed execution for the same reason we moved from running code as root to running it in containers. Isolation is not a limitation. It is a feature.

The demand OpenClaw proved is real. Autonomous AI agents that execute code, manage files, and automate workflows -- that is the future. The question is whether that future runs on your bare machine or inside a sandbox designed for it.
