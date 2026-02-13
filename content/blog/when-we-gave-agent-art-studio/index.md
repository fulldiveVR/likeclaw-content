---
title: "When We Gave Our Agent an Art Studio"
description: "How adding AI image generation turned a productivity tool into a creative platform."
date: 2026-02-08
draft: false
images: ["cover.jpg"]
tags: ["building-in-public", "ai-agents", "multi-model"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["from-chat-to-agent-platform", "teaching-ai-to-schedule-itself"]
sections:
  - type: hero
  - type: content
  - type: steps
    heading: "From text-only to full creative studio"
    items:
      - title: "Start with basic image generation"
        description: "Day 22: Added the first image generation tool. Users could generate images during conversations. Simple, but a door opened."
      - title: "Add Replicate-based tools"
        description: "Day 30: Integrated Replicate's model ecosystem. Suddenly we had access to dozens of image models — not just one."
      - title: "Build the Studio workspace"
        description: "Day 36: Created a dedicated creative workspace with a Salvador Dali-inspired agent. Different tools, different personality, different purpose."
      - title: "Protect with billing"
        description: "Day 34: Added subscription guards specifically for image generation. Creative tools are expensive to run — billing awareness was already built in."
  - type: faq
    heading: "Questions about AI creative tools"
    items:
      - question: "Which image models are available?"
        answer: "Multiple models through Replicate and our multi-model infrastructure, including various Stable Diffusion variants and specialized models. The specific models evolve as the ecosystem improves."
      - question: "Can I use generated images commercially?"
        answer: "That depends on the specific model used to generate the image. We recommend checking the license terms of each model. Most open models allow commercial use."
      - question: "How does image generation billing work?"
        answer: "Image generation uses sandbox execution credits. Free tier users can't access image generation. Pro and Power users have it included in their execution allowance."
---

## The day our chat app learned to paint

December 21, 2025. One month after the first commit. Our platform could chat, manage files, schedule tasks, and run code. It was a solid productivity tool.

Then we gave it eyes. And hands. And an art studio.

We added AI image generation. Not as a separate product. Not as a "creative module" behind a different URL. As a natural extension of what the AI agent could already do.

"Write me a blog post about cloud security and generate a header image for it." One conversation. One agent. Text and visuals, together.

## Why creative tools matter for a productivity platform

On the surface, image generation seems like a strange addition to a platform built for developers and founders. These are people who write code and analyze data. They don't "make art."

Except they do.

Every pitch deck needs visuals. Every blog post needs a header. Every product page needs screenshots and mockups. Every social media post needs an image. Developers and founders create visual content constantly — they just don't think of it as "creative work."

Before LikeClaw's Studio, the workflow looked like this: write the content in one tool, open Midjourney in another tab, generate an image, download it, upload it to the content tool. Four context switches for one image.

After: "Generate an image for this content." Done. The image appears in the conversation. Save it to the workspace. It's right there with the text it belongs to.

## The Salvador Dali agent

This is where things got fun.

When we built the Studio workspace, we didn't just add image generation tools to the existing chat agent. We created a dedicated creative agent — inspired by Salvador Dali's surrealist approach to art.

The Studio agent thinks differently than the productivity agent. It's more experimental. More willing to suggest unexpected directions. When you ask for "a logo for a tech company," it doesn't just generate a generic blue shield. It asks questions. What feeling do you want? What's your audience? What should this absolutely NOT look like?

Different workspaces, different agents, different personalities. That's the power of the workspace model we built in week one. Each workspace is a context — and context shapes behavior.

## The billing lesson

Here's something we learned the hard way: image generation is expensive. Each generation costs real money in GPU time. Without billing guards, a user on the free tier could rack up significant costs.

Remember how we built billing on day three? This is where it paid off.

When we added image generation, we simply tagged the image tools as "requires subscription." The billing guard we built weeks ago handled the rest. Free tier users see a clear message: "Image generation requires a Pro or Power subscription." No surprise bills. No awkward conversations.

One team member pushed the subscription protection code on Christmas Day, 2025. The commit message: "feat: add protection to image generation tools when user doesn't have a subscription." Even on holidays, the billing-first approach kept paying dividends.

## The broader pattern

Image generation was the first time we added a capability that felt "different" from the core product. It wasn't chat. It wasn't file management. It wasn't code execution. It was creative output.

But the architecture absorbed it seamlessly. The workspace model, the agent system, the billing guards, the file storage — everything we'd built in the first month supported this new capability without modification.

That's the test of good architecture: can it absorb a feature that the architects didn't anticipate? For us, the answer was yes. And it gave us confidence that the next unexpected feature — whatever it turns out to be — will fit just as naturally.

The AI agent that started as a chat interface now writes, codes, analyzes, schedules, and creates visual art. Not because we planned all of that on day one. But because we built a foundation that could grow.
