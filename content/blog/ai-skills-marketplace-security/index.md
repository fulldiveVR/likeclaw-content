---
title: "AI Skills Marketplaces: Why Open Registries Are a Security Nightmare"
description: "341 malicious skills on ClawHub. 36% contain prompt injection. Here's what a secure skills marketplace looks like."
date: 2026-02-12
draft: false
tags: ["security", "marketplace", "openclaw", "ai-agents"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["code-execution", "task-automation"]
related_blog_posts: ["openclaw-security-what-you-need-to-know", "sandboxed-ai-agents-future"]
sections:
  - type: hero
  - type: content
  - type: metrics
    headline: "ClawHub by the numbers"
    items:
      - label: "Total skills on ClawHub"
        value: "5,705"
        source: "ClawHub Registry, Feb 2026"
      - label: "Confirmed malicious"
        value: "341+"
        source: "Snyk Research, Feb 2026"
      - label: "Prompt injection rate"
        value: "36%"
        source: "Snyk ToxicSkills Report"
      - label: "macOS stealer packages"
        value: "335"
        source: "Snyk Research, Feb 2026"
  - type: before_after
    before:
      summary: "Open skill registry (ClawHub model)"
      items:
        - "Anyone can publish with a 1-week-old GitHub account"
        - "No code review or security scanning"
        - "Skills run with full system access"
        - "335 packages installed macOS stealer malware"
    after:
      summary: "Vetted skill marketplace (LikeClaw model)"
      items:
        - "Mandatory security review before publishing"
        - "Automated scanning + human review"
        - "Skills run in sandboxed containers"
        - "0 malware incidents by architecture"
  - type: faq
    heading: "Common questions about skill marketplace security"
    items:
      - question: "How does LikeClaw vet skills before they go live?"
        answer: "Every skill submitted to the LikeClaw marketplace goes through a two-stage review: automated static analysis and dependency scanning, followed by human code review. Skills are then tested in an isolated sandbox environment before approval. No skill reaches users without passing both stages."
      - question: "Can I import my existing OpenClaw skills into LikeClaw?"
        answer: "We are building migration tooling for OpenClaw skill compatibility. Imported skills go through the same mandatory security review as new submissions. You will not be able to bypass the vetting process, but the format translation is handled automatically."
      - question: "Can I publish my own skills on the LikeClaw marketplace?"
        answer: "Yes. Any user can submit a skill for review. You write the skill, submit it, and our review pipeline handles the rest. Approved skills are published to the marketplace and available to all users. Rejected skills receive specific feedback on what to fix."
      - question: "How do I know if a skill on the marketplace is trustworthy?"
        answer: "Every skill in the LikeClaw marketplace has passed automated scanning and human review. Skills also run inside sandboxed containers with scoped permissions, so even if a skill behaved unexpectedly, it cannot access your system, files, or credentials outside its container."
---

## The appeal of AI skill marketplaces

AI agent skill marketplaces are a genuinely good idea. Instead of building every automation from scratch, you browse a registry, install a pre-built skill, and your agent gains a new capability in seconds. Email triage, calendar management, code review, data pipeline orchestration -- community-built skills let you skip the boilerplate and get to the result.

OpenClaw's ClawHub registry has 5,705 community-built skills as of February 2026. The categories span everything from crypto trading and DeFi automation to productivity workflows and social media management. The growth is real. The demand is real. People want reusable AI agent capabilities, and they want them from a community that builds faster than any single vendor can.

The concept works. The implementation is the problem.

## The problem with open registries

ClawHub operates as an open registry. Anyone with a GitHub account that is at least one week old can publish a skill. There is no code review. There is no sandboxing. There is no vetting process. You write a `SKILL.md` file with YAML frontmatter, push it to the registry, and it becomes available to every OpenClaw user on the planet.

This is the same trust model that npm and PyPI used for years before supply chain attacks became an industry-wide crisis. The difference is that AI agent skills are not just libraries imported into a codebase -- they are instructions that an autonomous agent executes with full system access. A malicious npm package can compromise a build pipeline. A malicious AI agent skill can compromise an entire machine in real time.

## What the researchers found

In February 2026, Snyk published its [ToxicSkills report](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) documenting **341 confirmed malicious skills** on ClawHub. Of those, **335 used fake prerequisite checks to install macOS stealer malware** -- specifically Atomic Stealer (AMOS), a well-known credential harvester that exfiltrates passwords, browser cookies, cryptocurrency wallets, and keychain data.

The attack pattern was straightforward. A skill would declare a system dependency in its prerequisites. When the user's agent attempted to satisfy that dependency, it would execute a shell command that downloaded and ran the stealer binary. The user never saw a prompt. The agent, doing what agents do, tried to be helpful.

Separately, Snyk's analysis found that **36% of ClawHub skills contain prompt injection** -- hidden instructions embedded in skill definitions designed to manipulate the agent's behavior. And Cisco's security team independently [demonstrated data exfiltration](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) through a third-party skill that silently forwarded conversation context to an external server.

These are not theoretical attacks. They are documented, confirmed, and in some cases still live on the registry.

## Supply chain attacks are the new vector

If this sounds familiar, it should. The software industry spent the last five years learning that open package registries are a prime target for supply chain attacks. Malicious packages on npm. Typosquatting on PyPI. Dependency confusion targeting internal registries. The pattern is well-established: attackers publish something that looks useful, wait for unsuspecting users to install it, and execute their payload.

AI agent skill marketplaces inherit every one of these risks, plus a new one: the skills do not just import code -- they give instructions to an autonomous agent with system access. The attack surface is not a build server. It is your entire machine. Your filesystem. Your credentials. Your browser sessions.

When Computerworld [called OpenClaw "a security nightmare"](https://www.computerworld.com), they were not exaggerating. When Gary Marcus called it ["a disaster waiting to happen"](https://garymarcus.substack.com/p/openclaw-aka-moltbot-is-everywhere), the disaster had already happened 341 times.

## What a secure skills marketplace looks like

The answer is not to abandon skill marketplaces. The answer is to build them with security as the foundation, not an afterthought. A secure skills marketplace needs five things:

**Mandatory code review.** Every skill submission goes through automated static analysis and human review before it reaches users. No exceptions. No fast track for popular publishers.

**Sandbox testing before approval.** Skills are executed in an isolated environment during the review process. Reviewers observe what the skill actually does -- what it accesses, what it downloads, what it sends over the network -- not just what it claims to do.

**Runtime isolation.** Even after approval, skills run inside sandboxed containers. If a skill somehow passes review with hidden behavior, the sandbox limits the blast radius. It cannot access the host filesystem, other users' data, or system credentials.

**Permission scoping.** Skills declare the permissions they need. File access, network access, specific API endpoints. The runtime enforces these declarations. A calendar skill has no business reading your SSH keys.

**Community reporting.** Users can flag suspicious behavior. Flagged skills are pulled from the marketplace and re-reviewed. The feedback loop is continuous.

## How LikeClaw handles this

At LikeClaw, every skill in the marketplace passes a mandatory security review before publishing. Skills are tested inside [E2B sandboxed containers](/blog/sandboxed-ai-agents-future/) -- the same isolation technology that protects your tasks at runtime. Automated scanning checks for known malware signatures, dependency vulnerabilities, and prompt injection patterns. Human reviewers verify the results.

At runtime, skills execute inside isolated containers with scoped permissions. A skill cannot access your filesystem, your credentials, or your network beyond what it explicitly declares and what the sandbox allows. If a skill tried the same fake-prerequisite attack that compromised 335 ClawHub users, the sandbox would contain it. The malware would download into a container that gets destroyed after execution. Your machine stays untouched.

This is the difference between an open registry and a vetted marketplace. One trusts the community to police itself. The other verifies, then trusts.

For a deeper look at the security issues with OpenClaw's architecture, see our breakdown in [OpenClaw Security: What You Need to Know](/blog/openclaw-security-what-you-need-to-know/). For a side-by-side comparison of the two approaches, see [LikeClaw vs OpenClaw](/comparisons/likeclaw-vs-openclaw/).

The demand for AI agent skills is not going away. The question is whether you install them from a registry where 6% of submissions are confirmed malware, or from a marketplace where every skill has been reviewed, tested, and sandboxed before it reaches your agent.
