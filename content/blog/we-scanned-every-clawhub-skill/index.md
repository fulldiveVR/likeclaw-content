---
title: "We Scanned 5,327 ClawHub Skills. 65 Were Dangerous."
description: "We built an automated pipeline to analyze every skill on OpenClaw's marketplace. Here's what we found — and what we filter out."
date: 2026-02-13
draft: true
images: ["cover.jpg"]
tags: ["security", "marketplace", "openclaw", "ai-agents", "building-in-public"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["code-execution", "task-automation"]
related_blog_posts: ["skills-marketplace-without-malware", "ai-skills-marketplace-security"]
sections:
  - type: hero
  - type: metrics
    headline: "What we found inside ClawHub"
    items:
      - label: "Skills scanned"
        value: "5,327"
        source: "LikeClaw internal scan, Feb 2026"
      - label: "Flagged as dangerous"
        value: "65"
        source: "AI + manual review"
      - label: "Data exfiltration skills"
        value: "20+"
        source: "Sending user data to unknown servers"
      - label: "Credential theft skills"
        value: "10+"
        source: "Harvesting API keys, passwords, wallets"
  - type: content
  - type: comparison_table
    heading: "Threat categories we detected"
    columns:
      - name: "Threat type"
        highlight: true
      - name: "Skills found"
        highlight: false
      - name: "Severity"
        highlight: false
    rows:
      - label: "Malware / RCE"
        values: ["Remote code execution, arbitrary binary download", "7", "Critical"]
        highlights: ["error", "default", "error"]
      - label: "Data exfiltration"
        values: ["User data sent to unknown external servers", "17+", "High"]
        highlights: ["error", "default", "error"]
      - label: "Credential theft"
        values: ["Passwords, API keys, wallet keys harvested", "10", "High"]
        highlights: ["error", "default", "error"]
      - label: "Suspicious PDF ring"
        values: ["7 skills routing PDFs to xss-cross-service-solutions.com", "7", "High"]
        highlights: ["error", "default", "error"]
      - label: "Crypto / financial risk"
        values: ["Wallet private keys required, automated transfers", "8", "Medium"]
        highlights: ["default", "default", "default"]
      - label: "Supply chain attacks"
        values: ["Downloading unverified binaries, curl|bash patterns", "6", "Medium"]
        highlights: ["default", "default", "default"]
      - label: "SSL/TLS disabled"
        values: ["Certificate verification turned off, MITM vulnerable", "3", "Medium"]
        highlights: ["default", "default", "default"]
      - label: "Destructive actions"
        values: ["rm -rf, arbitrary command execution, root access", "7", "Medium"]
        highlights: ["default", "default", "default"]
    footer: "Source: LikeClaw internal scan of ClawHub marketplace, February 2026"
  - type: faq
    heading: "Questions about our scanning process"
    items:
      - question: "Does this mean every other ClawHub skill is safe?"
        answer: "No. Our scan catches known dangerous patterns, but no automated system is perfect. Skills can hide malicious behavior behind obfuscation, delayed execution, or update-based attacks where safe code is replaced after publication. We treat our scan as a strong filter, not a guarantee."
      - question: "How do you handle skills that are borderline?"
        answer: "Skills that are flagged by automated analysis go through manual review. Some skills have legitimate reasons for behaviors that look suspicious — a deployment tool might genuinely need SSH access, for example. Context matters, and the final decision is human."
      - question: "Can I still use these skills on OpenClaw?"
        answer: "Yes — ClawHub does not remove skills based on our analysis. These skills are still live and installable on OpenClaw. That is the point. On LikeClaw, they are filtered out automatically and would not pass our review process."
      - question: "Will you publish the full list of flagged skills?"
        answer: "We are evaluating responsible disclosure. Some of these skills are clearly malicious and their authors know it. Others may be poorly written rather than intentionally harmful. We have reported the most critical findings to ClawHub."
      - question: "What if a dangerous skill gets past your filter?"
        answer: "Our scanning pipeline is one layer of defense, not the only one. Even if a skill passed the filter, it would still need to pass human review before appearing in our marketplace. And even if it passed review, it would run inside an E2B sandbox — an isolated container that gets destroyed after execution. Your system stays untouched."
  - type: cta
    heading: "A skills marketplace you can actually trust"
    subheading: "Every skill scanned. Every execution sandboxed. No surprises."
---

## Why we scanned every skill on ClawHub

We are building a skills marketplace for LikeClaw. To populate it, we import skills from ClawHub — OpenClaw's community registry of 7,000+ skills. But we refuse to import blindly. Snyk already found [341 confirmed malicious skills](/blog/ai-skills-marketplace-security/) on that registry. We needed to know exactly what we were dealing with.

So we built a pipeline that downloads, parses, and analyzes every single skill on ClawHub. Not a sample. Not the top 100. All of them.

The result: out of 5,327 skills that passed our initial compatibility filter, **65 were flagged as dangerous**. That is 1.2% of the marketplace. One in every 83 skills wants to do something it should not.

Here is what we found, how we found it, and what we do about it.

## How the scanning pipeline works

Our detection runs in three stages.

**Stage 1: Download the entire marketplace.** A Python script paginates through the ClawHub API, downloading every skill's source code, metadata, and file contents to local storage. Rate-limited at 1.8 requests per second with exponential backoff. The most recent run pulled 7,001 skill directories.

**Stage 2: Platform compatibility filter.** Before security analysis, we filter for E2B sandbox compatibility. Skills that require macOS-only binaries (osascript, pbcopy, Homebrew), Docker containers, or raw system access are flagged as incompatible and hidden. This filter checks declared dependencies, scans source code for platform-specific patterns, and validates against a blocklist of 39 known incompatible binaries. This stage removed 114 skills — leaving 5,327 for security analysis.

**Stage 3: AI-powered source code analysis.** Every remaining skill's full source code is concatenated and sent to an LLM for safety assessment. The model evaluates each skill against five criteria:

- Does it exfiltrate data to unknown endpoints?
- Does it run destructive commands?
- Does it attempt prompt injection or jailbreaking?
- Does it access sensitive system resources without clear purpose?
- Does it contain obfuscated or suspicious code?

The model returns a structured verdict: safe or unsafe, a category, a description of what the code actually does (not what the marketing claims), and safety notes explaining any concerns.

The full run analyzed 5,213 skills over approximately 13.5 hours. Zero failures. 65 skills flagged as unsafe. Every one of those 65 was subsequently marked `hidden` in our database and excluded from our marketplace.

## The seven threat patterns we found

The 65 dangerous skills cluster into distinct attack patterns. Some are brazen. Some are subtle. A few are coordinated.

### Pattern 1: Straight-up malware

Seven skills crossed the line from "questionable" into "clearly malicious." The worst offender — a skill called **redpacket-claim** — downloads and executes an arbitrary binary from a hardcoded IP address (120.48.191.124) with no verification, no signature check, no user prompt. You install it, and it runs whatever the server sends.

Another, **self-evolve**, authorizes its agent to execute bash commands, modify system configurations, and alter files without any confirmation step. A third, **bun-runtime**, uses `eval` to execute arbitrary shell commands passed as strings — the oldest and most dangerous pattern in software security.

These are not ambiguous. These are remote code execution delivered through a skill marketplace.

### Pattern 2: The PDF exfiltration ring

This was the most surprising finding. Seven seemingly unrelated skills — **add-watermark-to-pdf**, **compress-pdf**, **merge-pdf**, **change-pdf-permissions**, **make-pdf-safe**, **password-protect-pdf**, and **remove-password-from-pdf** — all route user-uploaded PDFs to the same domain: `api.xss-cross-service-solutions.com`.

Seven skills. One domain. A domain with "xss" in the name.

Users who install any of these skills and hand them a PDF are sending their documents — contracts, financial statements, personal records — to a single external server. The skills look independent. They have different names, different descriptions, different apparent authors. But they all phone home to the same place.

This looks like a coordinated campaign to harvest PDF content at scale.

### Pattern 3: Credential harvesting

Ten skills either expose credentials directly or transmit them to third parties.

Two skills branded as **Twitter Command Center** (one for search + monitor, another for search + post) send users' Twitter email and password to `api.aisa.one` — a third-party automation API. The skill asks for your Twitter credentials to "help you manage your account." Then it sends them to someone else's server.

**coconala-seller** forwards login credentials to an external browser automation service. **paytrigo-openclawbot** ships with hardcoded live API keys in its source code — anyone who reads the source can access those accounts. **voice-agent** mounts the user's AWS credentials directory (`~/.aws`) into a Docker container that it controls.

**uniclaw** is particularly concerning: it accesses the user's wallet mnemonic and private key while containing a hardcoded API key in its own source. That is a combination purpose-built for draining cryptocurrency wallets.

### Pattern 4: Silent data exfiltration

The largest category. Over 17 skills send user data to external servers that users never agreed to share with.

**conversation-summary** sends your full conversation history to `iautomark.sdm.qq.com`. **voidborne** exfiltrates your machine ID, hostname, username, and generated content to `voidborne.org`. **clawcredit** sends your agent's entire reasoning trace — prompts, logic, and responses — to an external backend. **telegram-body-scan** forwards sensitive video data (body scans) to an external service.

**clawswarm** sends registration data, reasoning traces, and solutions to `claw-swarm.com`. **clawdrug** sends inputs and outputs to an external API while also downloading remote prompt templates that can modify the agent's behavior. **trade-with-taro** exfiltrates knowledge content to `kairyuu.net`.

In every case, the skill's description says nothing about this data sharing. Users have no idea their conversations, files, and agent outputs are being forwarded to third-party servers.

### Pattern 5: Crypto wallet exposure

Eight skills require your cryptocurrency wallet's private key to function. **lobsterhood** automates USDC transfers without confirmation — a single misconfigured rule could drain a wallet. **mia-polymarket-trader** requires private keys for automated trading. **bonero-miner** runs CPU-intensive mining operations, encouraging users to execute unverified install scripts via the classic `curl | bash` pattern.

These skills sit at the intersection of financial risk and supply chain risk. You give them your private key, and they execute code you did not write and cannot verify.

### Pattern 6: Supply chain attacks

Six skills download and execute unverified code from external URLs. **MoltiumV2** fetches and runs code from `moltium.fun`. **desktop-sandbox** downloads installer binaries from GitHub and runs them with system privileges. **xiaohongshu** requires sudo access to install system packages from unverified sources.

The pattern is always the same: the skill claims to need a dependency, downloads it from an URL the user cannot verify, and executes it. This is the exact attack vector that Snyk documented in the 335 macOS stealer cases — but with different payloads.

### Pattern 7: XSS and prompt injection

Three skills are explicit proof-of-concept attacks against the ClawHub platform itself. **localstorage-poc** uses SVG-embedded JavaScript to access authentication tokens from localStorage, then pings an external endpoint with the token count. **red-pill** loads an external iframe from `clawdhub.com` through an SVG XSS vector.

These skills demonstrate that ClawHub's own platform is vulnerable to cross-site scripting through its skill rendering pipeline. They exist on the marketplace as working exploits.

## What we do with the results

Every skill flagged as unsafe is automatically hidden in our database. It never appears in skill listings, search results, or the skill picker. Users cannot install it.

But automated scanning is only the first gate. Our full pipeline has three layers:

1. **Automated analysis** catches the 65 skills described in this post — the obviously dangerous ones.
2. **Human review** evaluates every skill before it appears in our marketplace. Some behaviors that look suspicious have legitimate explanations. Some behaviors that look safe are actually dangerous. The final call is human.
3. **Sandboxed execution** means that even if a skill somehow passed both filters, it runs inside an [E2B container](/blog/what-is-e2b-sandboxed-execution/) — an isolated environment that is created per task and destroyed after. A malicious skill inside a sandbox is a malicious skill with nowhere to go.

## What this does not catch

We want to be transparent about the limits.

Our scanning pipeline is strong but not infallible. It will miss skills that:

- **Obfuscate their behavior.** Base64-encoded payloads, steganography, or multi-stage attacks where each stage looks benign individually.
- **Use time-delayed execution.** A skill that behaves normally for weeks, then activates malicious code on a trigger.
- **Update after publication.** A skill that passes review, then pushes a malicious update. (Our pipeline re-scans periodically, but there is always a window.)
- **Exploit zero-day vulnerabilities.** Attacks that target unknown weaknesses in the sandbox or runtime environment.

No automated system catches everything. We make no guarantee that our marketplace is free of all risk. What we guarantee is that we are actively looking, we filter out what we find, and the sandbox limits the blast radius of anything that gets through.

This is fundamentally different from a marketplace that does not look at all.

## The numbers, in context

65 dangerous skills out of 5,327 is a 1.2% rate. That sounds small until you consider the math of a growing marketplace.

At 5,327 skills, 1.2% means 65 landmines. At 10,000 skills, it means 120. At 50,000 skills, it means 600. Open registries scale their attack surface at the same rate they scale their value. Every new skill is either useful or dangerous, and without systematic scanning, users have no way to tell the difference.

Snyk's independent research found 341 confirmed malicious skills on ClawHub — a higher absolute number because their analysis covered different time periods and detection criteria. Our 65 is not a contradiction of their findings. It is a separate scan with a different methodology that confirms the same conclusion: the ClawHub marketplace has a systemic safety problem.

The skills we flagged are still live on ClawHub. They are still installable. Users who run OpenClaw can still install them today.

On LikeClaw, they are filtered, reviewed, and sandboxed. That is the difference between an open registry and a vetted marketplace.
