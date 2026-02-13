---
title: "Building Onboarding That Feels Like a Conversation"
description: "How we designed a welcome experience that guides users without patronizing them — in four languages, across multiple workspaces."
date: 2026-02-01
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "onboarding", "startup"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: ["email-automation"]
related_blog_posts: ["day-one-was-global-day", "first-commit-to-live-in-48-hours"]
sections:
  - type: hero
  - type: content
  - type: before_after
    before:
      summary: "Traditional onboarding"
      items:
        - "Five-step wizard you can't skip"
        - "Generic tooltips pointing at obvious buttons"
        - "Congratulatory confetti for clicking 'Next'"
        - "A tour that shows you everything but teaches you nothing"
    after:
      summary: "Conversational onboarding"
      items:
        - "A welcome message from the AI agent itself"
        - "Different messages for different workspaces"
        - "Shows only once — then gets out of your way"
        - "In your language, from the first moment"
  - type: faq
    heading: "Questions about our onboarding approach"
    items:
      - question: "What happens if I skip the onboarding?"
        answer: "Nothing bad. The welcome message appears once. The feature modals appear once. After that, the product gets out of your way. There's no penalty for skipping, no locked features, no 'complete your profile to continue.'"
      - question: "Is the onboarding the same in every language?"
        answer: "The structure is the same, but the content is localized for each language. Not machine-translated — reviewed and adapted for cultural context."
      - question: "Do different workspace types have different onboarding?"
        answer: "Yes. A creative workspace (Studio) welcomes you differently than a general workspace. The welcome message highlights the tools and capabilities relevant to that specific workspace."
  - type: cta
    heading: "Start in 30 seconds"
    subheading: "No tutorials required. Your AI agent welcomes you personally."
---

## The onboarding problem nobody talks about

Here's the dirty secret of product onboarding: most of it is theater.

Product tours that show you buttons you can see yourself. Tooltips that explain what "Save" means. Progress bars that track how much of the tour you've endured. Five-step wizards that exist because someone in a meeting said "we need better onboarding."

Users don't need to be shown around. They need to understand what the product can do for them. And the best way to demonstrate what an AI agent can do is to let the AI agent demonstrate it.

## December 13, 2025: onboarding week

Three weeks after the first commit, we tackled onboarding. Not because we had spare time — because users were signing up and bouncing. They'd see the interface, not know what to do, and leave.

The typical solution: add a product tour. Walk users through the UI. Show them where the buttons are. Maybe add some animated arrows.

We did something different. We let the AI introduce itself.

## The welcome message approach

When a user opens LikeClaw for the first time, their default workspace already has a conversation waiting. The AI agent has sent them a message:

"Welcome. I'm your AI assistant. I can help you with research, writing, data analysis, code, and more. Try asking me something, or explore your workspace — you have a file system on the right where I can save my work for you."

That's it. No tour. No wizard. No progress bar. Just the AI telling you what it can do, in a natural conversational format.

The brilliance is subtle: by reading the welcome message, the user is already in the product's core interaction mode. They're reading a chat message. The next natural action is to type a response. They're onboarded by using the product, not by watching a presentation about the product.

## Context-aware welcomes

Not every workspace is the same, so not every welcome should be the same.

The general workspace welcome focuses on versatility: I can help with research, writing, analysis, coding.

The Studio workspace welcome focuses on creativity: I can generate images, create visual content, help with design concepts.

Each workspace has its own personality, and the welcome message reflects that personality. A user who creates a coding workspace sees a message about code review and debugging. A user who creates a marketing workspace sees a message about content and analysis.

The welcome message isn't a generic greeting. It's a demonstration of the workspace's capabilities.

## Feature modals that teach, once

Beyond the welcome message, we added feature explanation modals. These are brief overlays that explain a specific capability — like scheduling or file sharing — the first time a user encounters that feature.

Key design decision: **show once, never again.** We store a flag per user per modal. Once you've seen the scheduling explanation, it never appears again. Not on refresh. Not on a different device. Gone forever.

This matters because nothing destroys trust faster than a product that repeatedly explains itself. "I know what this button does. Stop telling me." If a user sees a modal once and doesn't need the explanation, they close it in two seconds and move on. If a user sees the same modal for the tenth time, they start resenting the product.

## Four languages from the start

Every welcome message, every feature modal, every onboarding touchpoint is available in English, Russian, Simplified Chinese, and Traditional Chinese. Not as an afterthought — as a first-class implementation.

This is where the i18n investment from week one paid off. When we built the onboarding, the translation pipeline was already in place. Write the English welcome message. Run the translator. Review the output. Commit. Four languages, one workflow.

A user in Taipei sees the welcome message in Traditional Chinese. Not broken characters. Not a half-translated interface. A complete, coherent welcome in their language.

## What we measured

Before onboarding: users would sign up, see the interface, and about 40% would leave without sending a single message.

After onboarding: that number dropped significantly. The welcome message gave users a starting point. Instead of staring at an empty chat and wondering what to do, they had something to respond to.

The most common first message after reading the welcome? Some variant of "OK, help me with [specific task]." The welcome message turned "what is this?" into "let me try something." That's the entire goal of onboarding in one sentence.

## The anti-pattern we avoided

We could have built a "Getting Started" checklist. Complete your profile. Create a workspace. Upload a file. Send your first message. Connect an integration. Each step with a checkbox and a reward animation.

That pattern works for products where users need to configure things before they can use them. It doesn't work for products that should work immediately.

LikeClaw works the moment you sign up. There's nothing to configure. Nothing to connect. Nothing to complete. You just start talking to the AI, and it starts helping.

Our onboarding reflects that: a welcome message that says "I'm here, I'm ready, what do you need?" Not "please complete these five steps before I can help you."

The best onboarding doesn't feel like onboarding. It feels like the product already knows you.
