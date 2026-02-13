---
title: "Day One Was Global Day"
description: "Why we added four languages in week one — and used AI to do it."
date: 2026-02-11
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "internationalization", "startup"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["first-commit-to-live-in-48-hours", "from-chat-to-agent-platform"]
sections:
  - type: hero
  - type: metrics
    headline: "Global from week one"
    items:
      - label: "Languages supported"
        value: "4"
      - label: "Days to internationalize"
        value: "3"
      - label: "Manual translations"
        value: "0"
  - type: content
  - type: cards
    heading: "Languages shipped in week one"
    items:
      - icon: "🇺🇸"
        title: "English"
        description: "Primary language. Every string started here."
      - icon: "🇷🇺"
        title: "Russian"
        description: "Our founding team's native language. Built simultaneously."
      - icon: "🇨🇳"
        title: "Chinese (Simplified & Traditional)"
        description: "Two of the world's largest developer populations. Supported from day one."
  - type: faq
    heading: "Questions about going global early"
    items:
      - question: "Why not just do English first and translate later?"
        answer: "Because retrofitting i18n into an existing codebase is painful. Every hardcoded string becomes a bug. We added the i18n infrastructure in week one, which meant every feature we built afterward was automatically translation-ready."
      - question: "How accurate are AI-powered translations?"
        answer: "For a UI with short strings, buttons, and labels — surprisingly good. We review all translations, but the AI gets 90%+ right on the first pass. Good enough for week one. Refined over time."
      - question: "Will you add more languages?"
        answer: "Yes. The infrastructure supports any number of languages. The hard part was building the system. Adding a new language now takes hours, not weeks."
---

## Most startups localize last. We localized first.

By the end of our first week — before we had a billing page, before we had onboarding, before we had half the features we have today — LikeClaw spoke four languages: English, Russian, Simplified Chinese, and Traditional Chinese.

This wasn't a marketing stunt. It was an architectural decision that shaped everything that came after.

## The cost of "we'll translate later"

Here's what happens when a startup says "we'll add internationalization later":

They hardcode every string in English. Every button says "Submit." Every error says "Something went wrong." Every tooltip, every placeholder, every confirmation dialog — all embedded directly in the code.

Six months later, they want to enter the Chinese market. Now they need to find every hardcoded string across hundreds of files, extract them into translation files, wrap every text element in a translation function, test every screen in every language, and fix the fifty layouts that break because German words are longer than English ones.

That process takes weeks. Sometimes months. And it introduces bugs in screens that haven't been touched in months.

We decided to pay the cost upfront, when it was cheap.

## The AI translator

Here's where it gets interesting. Our team member Ruslan built an AI-powered translation system directly into our development workflow.

The process: write the English string, run the translator, get Russian, Simplified Chinese, and Traditional Chinese versions. Review. Commit. Done.

No spreadsheets. No translation agencies. No two-week turnaround times. The AI handles the grunt work. A native speaker reviews the output. The whole cycle takes minutes per batch of strings.

Is it perfect? No. Professional human translation will always be more nuanced. But for UI strings — "Save," "Delete," "New Workspace," "Your session has ended" — the AI nails it. And we ship in four languages instead of one.

## What this means for the product

When a developer in Shenzhen opens LikeClaw for the first time, they see it in their language. Not broken machine translation. Not a toggle buried in settings that switches to a half-translated interface. Real, complete support from the moment they land.

When a Russian-speaking founder uses our platform, their welcome message is in Russian. Their agent responses can be in Russian. Their workspace labels are in Russian.

This isn't just about translation. It's about respect. It says: we built this for you, not just for English-speaking San Francisco.

## The infrastructure pays for itself

Here's the part that surprised even us: the i18n infrastructure actually made development faster after the initial setup.

Every new feature starts with a translation key. That key is automatically available in four languages. The developer writes `t('workspace.settings.title')` instead of `"Workspace Settings"`. The translation file gets the English version. The AI fills in the rest.

There's no "localization sprint" at the end of a release cycle. There's no "we'll translate the new features later" ticket that sits in the backlog forever. Localization is baked into the development process. It's just how we build.

## Four languages is just the beginning

The i18n system we built supports any number of languages. The infrastructure is there. The translation pipeline is there. Adding Japanese or Korean or Spanish is a matter of running the translator and reviewing the output.

We started with four because those are the languages our team and early users speak. But the system was designed for forty.

Most companies treat internationalization as a growth-stage problem. We treated it as a day-one architecture decision. And that's made all the difference.
