# LikeClaw Content Guide

This is the single source of truth for creating content on the LikeClaw website. It covers everything: page types, the section system, front matter schemas, data files, and content guidelines.

---

## Table of Contents

1. [How the content system works](#1-how-the-content-system-works)
2. [Two ways to build a page](#2-two-ways-to-build-a-page)
3. [Page types and how to create them](#3-page-types-and-how-to-create-them)
4. [The sections system (composable pages)](#4-the-sections-system-composable-pages)
5. [Section type reference (all 15 types)](#5-section-type-reference-all-15-types)
6. [Recipes: common page patterns](#6-recipes-common-page-patterns)
7. [Data files (homepage content)](#7-data-files-homepage-content)
8. [Images, videos, and media](#8-images-videos-and-media)
9. [Cross-linking between pages](#9-cross-linking-between-pages)
10. [Content writing guidelines](#10-content-writing-guidelines)
11. [Rules and boundaries](#11-rules-and-boundaries)

---

## 1. How the content system works

The website is split into two repos:

| Repo | What it controls | Who edits it |
|------|-----------------|--------------|
| **Main repo** (`aiwize-com`) | Templates, CSS, layout, deployment | Engineers |
| **Content repo** (`likeclaw-content/`) | All text, images, data | Content creators |

As a content creator, you work **only** inside `likeclaw-content/`. You cannot break the site design — templates are locked in the main repo.

### File structure

```
likeclaw-content/
  content/
    use-cases/
      email-automation/       ← page bundle (directory)
        index.md              ← the page content
        hero.jpg              ← images bundled with the page
    blog/
      security-guide/
        index.md
        cover.jpg
    comparisons/
      likeclaw-vs-openclaw/
        index.md
    industries/
      saas/
        index.md
  data/
    hero.yaml                 ← homepage hero section
    stats.yaml                ← homepage stats bar
    features.yaml             ← homepage feature cards
    faq.yaml                  ← homepage FAQ
    cta.yaml                  ← shared CTA defaults
    ...
```

**Key concept: page bundles.** Every page is a directory containing `index.md` plus any images or videos. Media files go inside the page's directory, not in a shared folder.

---

## 2. Two ways to build a page

### Option A: Fixed layout (legacy, still works)

Each page type (use-case, blog, comparison, industry) has a built-in template with a predetermined section sequence. You fill in the front matter fields and write markdown. The template decides what goes where.

**When to use:** Quick pages where the default layout works fine.

### Option B: Composable sections (recommended for new pages)

Add a `sections:` array to front matter. You choose which sections appear and in what order. The template loops through your array and renders each section.

**When to use:** Any page where you want control over the layout — reorder sections, skip sections you don't need, add multiple of the same type.

### How the system decides which mode to use

```
Does the page have a `sections:` array in front matter?
  YES → render sections in order (composable mode)
  NO  → render the fixed template (legacy mode)
```

There is zero risk of breaking existing pages. If you don't add `sections:`, nothing changes. The fixed layout renders exactly as before.

---

## 3. Page types and how to create them

### Use Case (`content/use-cases/`)

Use cases show how LikeClaw solves a specific problem for a specific persona.

**To create one:**

1. Create directory: `content/use-cases/my-slug/` (slug = URL-friendly name, lowercase, hyphens)
2. Create `index.md` inside it
3. Add `hero.jpg` (1200x630px recommended — also becomes OG image for social sharing)
4. Set `draft: false` when ready to publish

**Fixed-layout front matter:**
```yaml
---
title: "Email Overload to Zero Inbox"
description: "AI agent saves 35 hours/month on email management."
date: 2026-02-01
draft: true
images: ["hero.jpg"]
tags: ["email", "productivity"]
categories: ["use-cases"]
persona: "Product Manager @ SaaS Startup"
industry: "saas"
difficulty: "beginner"            # beginner | intermediate | advanced
before:
  summary: "Manual email triage consuming 2+ hours daily"
  pain_points:
    - "Checked email 20+ times per day"
    - "Missing critical messages buried in noise"
after:
  summary: "AI monitors inbox 24/7, surfaces only what matters"
  outcomes:
    - "1.67 hours saved per day"
    - "Zero missed urgent emails"
roi:
  headline: "35 hours/month saved"
  metrics:
    - label: "Time saved daily"
      value: "1.67h"
    - label: "Monthly savings"
      value: "35h"
related_use_cases: ["code-review", "data-analysis"]
related_blog_posts: ["security-guide"]
implementation:
  integrations: ["Gmail", "Slack", "Notion"]
  steps:
    - "Connect Gmail via OAuth"
    - "Define priority rules"
    - "Enable auto-draft responses"
---

Your markdown content goes here.
```

**Fixed-layout renders in this order:** hero with badges → hero image → ROI metrics bar → before/after cards → markdown body → implementation steps → related pages → CTA.

### Blog Post (`content/blog/`)

**To create one:**

1. Create directory: `content/blog/my-post-slug/`
2. Create `index.md` inside it
3. Add `cover.jpg` for the blog card and OG image
4. Set `draft: false` when ready to publish

**Front matter:**
```yaml
---
title: "Why Sandboxed AI Agents Are the Future"
description: "OpenClaw proved the demand. Here's why security can't be an afterthought."
date: 2026-02-10
draft: true
images: ["cover.jpg"]
tags: ["security", "ai-agents"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0                    # 0 = auto-calculated from word count
related_use_cases: ["email-automation"]
---
```

**Fixed-layout renders:** date + author + reading time → title → cover image → markdown body → tags → related pages → CTA.

### Comparison (`content/comparisons/`)

**To create one:**

1. Create directory: `content/comparisons/likeclaw-vs-competitor/`
2. Create `index.md`
3. Set `draft: false` when ready to publish

**Front matter:**
```yaml
---
title: "LikeClaw vs OpenClaw"
description: "Feature-by-feature comparison: security, setup, pricing."
date: 2026-02-01
draft: true
images: ["og.png"]
tags: ["comparison"]
competitor: "OpenClaw"
competitor_url: "https://openclaw.ai"
verdict: "LikeClaw"
comparison_rows:
  - feature: "Setup time"
    us: "30 seconds"
    them: "3+ days"
    winner: "us"                   # us | them | tie
  - feature: "Code execution"
    us: "Sandboxed"
    them: "Raw system access"
    winner: "us"
related_use_cases: []
---

Optional markdown body with additional analysis.
```

**Fixed-layout renders:** title → comparison table → verdict → markdown body → related pages → CTA.

### Industry (`content/industries/`)

**To create one:**

1. Create directory: `content/industries/industry-slug/`
2. Create `index.md`
3. Add `hero.jpg` if desired
4. Set `draft: false` when ready to publish

**Front matter:**
```yaml
---
title: "LikeClaw for SaaS Companies"
description: "Automate development workflows, customer support, and internal ops."
date: 2026-02-01
draft: true
images: ["hero.jpg"]
tags: ["saas"]
industry_name: "SaaS"
target_roles: ["CTO", "Developer", "Product Manager"]
related_use_cases: ["email-automation", "code-review"]
---

Optional markdown body.
```

**Fixed-layout renders:** title + target role badges → hero image → markdown body → related use cases grid → CTA.

---

## 4. The sections system (composable pages)

### The problem sections solve

With fixed layouts, every use-case page has the same structure. You can't:
- Skip the before/after section if it doesn't apply
- Add a FAQ to one page but not another
- Put a testimonial between the metrics and the steps
- Add a comparison table to a use-case page

### How sections work

Add a `sections:` array to any page's front matter. Each entry is a building block with a `type` field. The page renders the sections top-to-bottom in the order you list them.

```yaml
---
title: "My Page"
description: "Page description"
sections:
  - type: hero
  - type: metrics
    headline: "Key results"
    items:
      - label: "Time saved"
        value: "35h/mo"
  - type: content
  - type: cta
---

This markdown body appears wherever `type: content` is placed.
```

### Rules

| Rule | Explanation |
|------|-------------|
| Only one `content` per page | The markdown body can only render once. Place `type: content` where you want it. |
| `hero` goes first | It renders the page title, description, and hero image. Put it at position 1. |
| `cta` goes last | The call-to-action section. It falls back to `data/cta.yaml` defaults if you don't override fields. |
| Order matters | Sections render top-to-bottom exactly as listed. Reorder the array to reorder the page. |
| All fields optional | Except `type`. Every other field in each section is optional unless marked "Required". |
| Works on any page type | Use cases, blog posts, comparisons, industries — all support `sections:`. |
| Backward compatible | No `sections:` array = fixed layout. Existing pages are unaffected. |

### What each section looks like

Every section renders as a full-width `<section>` block following the site's existing visual patterns. Sections alternate between white and light gray backgrounds. All styling is handled by templates — you just provide the data.

---

## 5. Section type reference (all 15 types)

### `hero`

**What it does:** Renders the page title (from `title:`), description (from `description:`), and badges for persona/industry/difficulty if present. Auto-detects a `hero.*` image from the page bundle.

**Fields:**
```yaml
- type: hero
  image: "custom-hero.jpg"     # Optional. Override auto-detected hero image.
```

**Notes:**
- Title, description, persona, industry, difficulty all come from the page's top-level front matter — you don't repeat them inside the section.
- If the page bundle contains `hero.jpg` or `hero.png`, it displays automatically. Use `image:` only to override with a different filename.

---

### `content`

**What it does:** Renders the markdown body (everything below the `---` front matter fence).

**Fields:**
```yaml
- type: content
```

**Notes:**
- No extra fields. Just `type: content`.
- Only use once per page.
- Position it wherever you want the prose to appear. Between metrics and steps? After the FAQ? Your choice.

---

### `text`

**What it does:** A centered text block. Good for mission statements, vision sections, or transition copy between other sections.

**Fields:**
```yaml
- type: text
  heading: "What if your AI ran in the cloud?"   # Main heading (supports &nbsp; for non-breaking spaces)
  paragraphs:                                      # Array of paragraphs
    - "First paragraph of body text."
    - "Second paragraph of body text."
  tagline: "This is autonomous AI with guardrails." # Optional. Bold closing statement.
```

**Visual:** Light gray background. Narrow centered column. Large heading, relaxed paragraph spacing.

---

### `metrics`

**What it does:** A horizontal bar of key statistics. Works like the ROI bar on use-case pages or the stats bar on the homepage.

**Fields:**
```yaml
- type: metrics
  headline: "35 hours/month saved"      # Bold centered headline above the numbers
  items:                                 # 2-4 items recommended
    - label: "Time saved daily"          # Small text below the number
      value: "1.67h"                     # The big bold number
      source: "Internal beta data"       # Optional. Tiny attribution text.
    - label: "Monthly savings"
      value: "35h"
    - label: "Emails auto-triaged"
      value: "94%"
```

**Visual:** Light gray background with border. Numbers in blue, large and bold. Labels in gray below.

---

### `before_after`

**What it does:** Two side-by-side cards. "Before" in red (pain points with X icons), "After" in green (outcomes with checkmark icons).

**Fields:**
```yaml
- type: before_after
  before:
    summary: "Checked email 20+ times per day"    # Brief problem statement
    items:                                          # Pain points (red X icons)
      - "Manual triage consuming 2+ hours daily"
      - "Missing critical messages buried in noise"
      - "Context-switching destroying deep work"
  after:
    summary: "AI monitors inbox 24/7"              # Brief solution statement
    items:                                          # Outcomes (green checkmark icons)
      - "1.67 hours saved per day"
      - "Zero missed urgent emails"
      - "Uninterrupted deep work blocks"
```

**Visual:** Two cards side-by-side on desktop, stacked on mobile. Before card has red-tinted background, After has green-tinted.

---

### `steps`

**What it does:** A numbered list of steps. Each step gets a blue circle with the number. Items can be simple strings or objects with a title and description.

**Fields:**
```yaml
- type: steps
  heading: "How to set this up"
  subheading: "Three steps, under 60 seconds."     # Optional
  items:
    # Simple format (string):
    - "Connect Gmail via OAuth"
    - "Define priority rules"
    - "Enable auto-draft responses"
    # Rich format (object with title + description):
    - title: "Connect your email"
      description: "Authorize Gmail or Outlook via OAuth. No passwords stored."
    - title: "Define priority rules"
      description: "Tell the agent what matters: VIP senders, keywords, labels."
```

**Notes:** You can mix simple strings and rich objects in the same list. Numbers are auto-generated (1, 2, 3...).

**Visual:** Light gray background. Blue numbered circles on the left, text on the right.

---

### `features`

**What it does:** A 3-column grid of feature cards. Each card has an optional colored badge, title, description, and bullet list.

**Fields:**
```yaml
- type: features
  heading: "Built for security. Designed for speed."
  items:
    - title: "Sandboxed. For Real."
      description: "Every execution runs in an isolated container."
      badge: "Security"                  # Optional. Badge label text.
      badge_color: "green"               # green | blue | neutral (default: neutral)
      bullets:                           # Optional. Checkmark bullet list.
        - "Isolated sandbox per task"
        - "Keys encrypted, never plaintext"
    - title: "100+ Models. Pay Per Use."
      badge: "Multi-Model"
      badge_color: "blue"
      description: "Claude, GPT-4, Gemini, Llama — all available."
      bullets:
        - "Switch models mid-task"
        - "Pay only for what you use"
    - title: "Zero Setup"
      badge: "Speed"
      badge_color: "neutral"
      description: "From signup to first result in 30 seconds."
      bullets:
        - "No install, no config"
        - "No API keys needed"
```

**Badge colors:**
- `green` — green background, green text (good for security, success themes)
- `blue` — blue background, blue text (good for features, tech themes)
- `neutral` — gray background, gray text (default)

**Visual:** Light gray background. 3 white cards on desktop, stacked on mobile. Cards have hover lift animation.

---

### `cards`

**What it does:** A simpler 3-column grid. Each card has an icon, title, and description. No badges, no bullet lists.

**Fields:**
```yaml
- type: cards
  heading: "The problems we solve"
  subheading: "AI agents shouldn't require a PhD to configure."  # Optional
  items:
    - icon: "⏱️"                  # Emoji or short text for the icon area
      title: "3+ days to configure"
      description: "Local environment setup, dependency management, permission configs."
    - icon: "🔓"
      title: "Your entire machine exposed"
      description: "Raw system access. Plaintext API keys."
    - icon: "💸"
      title: "$50-750/mo in surprise bills"
      description: "The software is free. The API costs aren't."
```

**Visual:** White background. Cards with light border, icon in a colored circle, hover lift. Good for problem statements or simple feature lists.

---

### `comparison_table`

**What it does:** A full comparison table with column headers, rows, and color-coded highlights. Matches the homepage comparison table.

**Fields:**
```yaml
- type: comparison_table
  heading: "How LikeClaw actually compares"
  columns:
    - name: "LikeClaw"
      highlight: true             # Bold column header
    - name: "OpenClaw"
      highlight: false
    - name: "ChatGPT Plus"
      mobile_hidden: true         # Hidden on small screens
  rows:
    - label: "Setup time"         # Row label (first column)
      values:                     # One value per column, in order
        - "30 seconds"
        - "3+ days"
        - "Instant (limited)"
      highlights:                 # Color coding per value. Options:
        - "brand"                 #   brand = bold black (winner)
        - "default"               #   default = gray
        - "default"               #   error = red (loser)
                                  #   success = green (winner, alternative)
                                  #   muted = light gray (irrelevant)
    - label: "Code execution"
      values: ["Secure sandbox", "Raw system access", "Limited interpreter"]
      highlights: ["brand", "error", "default"]
  footer: "Data as of February 2026."   # Optional footer below the table
```

**Highlight color options:**
| Value | Color | When to use |
|-------|-------|-------------|
| `brand` | Bold black | Our winning feature |
| `success` | Green | Positive outcome |
| `error` | Red | Competitor weakness |
| `muted` | Light gray | Not applicable / irrelevant |
| `default` | Gray | Neutral |

**Visual:** White background. Clean table with header borders. Highlighted column stands out. Scrollable on mobile.

---

### `testimonial`

**What it does:** A centered blockquote with the quote text, author name, role, and optional avatar image.

**Fields:**
```yaml
- type: testimonial
  quote: "I didn't realize how much time I was losing on email until I got it back."
  author: "Sarah Chen"
  role: "Product Lead"
  company: "Acme Corp"           # Optional
  image: "sarah.jpg"             # Optional. Filename in the page bundle.
```

**Notes:** Quotation marks are added automatically around the quote — don't include them in the `quote:` field.

**Visual:** Light gray background. Large italic quote text centered, author info below with optional circular avatar.

---

### `faq`

**What it does:** An accordion of questions and answers. Uses native HTML `<details>` — no JavaScript needed. Click a question to expand the answer.

**Fields:**
```yaml
- type: faq
  heading: "Common questions about email automation"
  items:
    - question: "Does LikeClaw read all my emails?"
      answer: "No. The agent only processes metadata for triage. Full content is accessed only when drafting responses, in an isolated sandbox."
    - question: "Can it handle multiple accounts?"
      answer: "Yes. Connect as many Gmail or Outlook accounts as you need."
    - question: "What if it drafts a bad response?"
      answer: "Auto-drafted responses are never sent automatically. They appear as drafts for you to review."
```

**Visual:** White background. Questions with a "+" icon that rotates to "x" when open. Answers slide open below.

---

### `cta`

**What it does:** A dark-background call-to-action section with a heading, subheading, and button. Falls back to `data/cta.yaml` for any fields you don't override.

**Fields:**
```yaml
- type: cta
  heading: "Ready to reclaim 35 hours/month?"     # Optional. Default: from data/cta.yaml
  subheading: "Join the beta. No credit card."     # Optional. Default: from data/cta.yaml
  button_label: "Start Free"                       # Optional. Default: from data/cta.yaml
  button_url: "/#early-access"                     # Optional. Default: /#early-access
```

**Notes:** The simplest CTA is just `- type: cta` with no fields. It will pull the heading, subheading, and button text from `data/cta.yaml` automatically. Only add fields to override the defaults for this specific page.

**Visual:** Dark (near-black) background. White heading, gray subheading, blue rounded button.

---

### `image`

**What it does:** A full-width image from the page bundle with optional alt text and caption.

**Fields:**
```yaml
- type: image
  src: "screenshot.png"          # Required. Filename in the page bundle.
  alt: "Dashboard screenshot"    # Optional. Alt text for accessibility.
  caption: "The LikeClaw dashboard showing active tasks."  # Optional. Caption below.
```

**Visual:** Centered with rounded corners and a subtle shadow. Wider than the text column (1000px max). Caption in small gray text below.

---

### `video`

**What it does:** An HTML5 video player for a video file in the page bundle.

**Fields:**
```yaml
- type: video
  src: "demo.mp4"               # Required. Filename in the page bundle.
  poster: "poster.jpg"          # Optional. Still image shown before play.
  caption: "30-second setup demo."  # Optional. Caption below.
```

**Visual:** Same width and styling as `image`. Native browser video controls (play, pause, scrub, fullscreen).

---

### `logos`

**What it does:** A horizontal row of text pills/badges. Good for listing integrations, partners, tools, or tech stack.

**Fields:**
```yaml
- type: logos
  heading: "Integrations"        # Optional. Small uppercase heading above.
  items:
    - "Gmail"
    - "Outlook"
    - "Slack"
    - "Notion"
    - "Linear"
    - "Google Calendar"
```

**Visual:** Light gray background. Small centered heading. Rounded white pills with borders, wrapping to multiple lines on mobile.

---

## 6. Recipes: common page patterns

### Use case (full)

Best for flagship use cases with strong data points.

```yaml
sections:
  - type: hero
  - type: metrics
    headline: "Key results"
    items: [...]
  - type: before_after
    before: {...}
    after: {...}
  - type: content
  - type: steps
    heading: "How to set this up"
    items: [...]
  - type: logos
    heading: "Integrations"
    items: [...]
  - type: faq
    heading: "Questions about this use case"
    items: [...]
  - type: cta
```

### Use case (lightweight)

For simpler use cases without metrics or FAQ.

```yaml
sections:
  - type: hero
  - type: content
  - type: steps
    heading: "Quick start"
    items: [...]
  - type: cta
```

### Blog post with sections

Sections work on blog posts too. Useful for long-form comparison posts or guides.

```yaml
sections:
  - type: hero
  - type: content
  - type: comparison_table
    heading: "Feature comparison"
    columns: [...]
    rows: [...]
  - type: faq
    heading: "FAQ"
    items: [...]
  - type: cta
```

### Comparison page with sections

More powerful than the fixed comparison layout.

```yaml
sections:
  - type: hero
  - type: comparison_table
    heading: "Feature by feature"
    columns: [...]
    rows: [...]
  - type: before_after
    before:
      summary: "With the competitor"
      items: [...]
    after:
      summary: "With LikeClaw"
      items: [...]
  - type: content
  - type: testimonial
    quote: "..."
    author: "..."
    role: "..."
  - type: cta
```

### Landing page style

For marketing-heavy pages.

```yaml
sections:
  - type: hero
  - type: metrics
    headline: "..."
    items: [...]
  - type: text
    heading: "The big promise"
    paragraphs: [...]
    tagline: "..."
  - type: features
    heading: "Why us"
    items: [...]
  - type: cards
    heading: "The problems we solve"
    items: [...]
  - type: comparison_table
    heading: "How we compare"
    columns: [...]
    rows: [...]
  - type: testimonial
    quote: "..."
    author: "..."
    role: "..."
  - type: faq
    heading: "FAQ"
    items: [...]
  - type: cta
```

---

## 7. Data files (homepage content)

Data files in `data/` control the homepage. Edit the YAML values — don't change field names or structure.

### `data/hero.yaml`
```yaml
badge: ""            # Badge text above headline
headline: ""         # Main H1 (supports &nbsp; for non-breaking spaces)
subheadline: ""      # Supporting paragraph
cta_label: ""        # Button text
cta_placeholder: ""  # Email input placeholder
cta_subtext: ""      # Text below CTA (supports &middot;)
success_title: ""    # Post-signup heading
success_text: ""     # Post-signup paragraph
product_visual_label: ""
product_visual_hint: ""
```

### `data/stats.yaml`
Array of stat items (displayed in order):
```yaml
- value: "341+"
  label: "Malicious skills found in OpenClaw's marketplace"
  source: "Snyk Research, 2026"
```

### `data/problem.yaml`
```yaml
heading: ""
subheading: ""
cards:               # Exactly 3 cards
  - icon: ""         # clock | lock | dollar
    title: ""
    description: ""
```

### `data/solution.yaml`
```yaml
heading: ""
paragraphs: [""]     # Array of paragraph strings
tagline: ""          # Bold closing statement
```

### `data/how_it_works.yaml`
```yaml
heading: ""
subheading: ""
steps:               # Exactly 3 steps
  - number: "01"
    title: ""
    description: ""
cta_label: ""
cta_subtext: ""
```

### `data/features.yaml`
Array of feature cards:
```yaml
- title: ""
  badge: ""
  badge_color: ""    # green | blue | neutral
  description: ""
  items: [""]        # Bullet points (checkmark icons)
```

### `data/comparison.yaml`
```yaml
heading: ""
columns:
  - name: ""
    highlight: false
    mobile_hidden: false
rows:
  - label: ""
    values: ["", "", ""]
    highlights: ["brand", "default", "default"]
footer: ""
```

### `data/pricing.yaml`
```yaml
section_heading: ""
section_subheading: ""
section_footer: ""
plans:
  - name: ""
    price: ""
    period: ""
    description: ""
    highlight: false
    badge: ""
    features: [""]
    cta_text: ""
    note: ""
```

### `data/faq.yaml`
Array of Q&A pairs:
```yaml
- question: ""
  answer: ""
```

### `data/cta.yaml`
Shared CTA defaults (used by the `cta` section type as fallback):
```yaml
heading: ""
subheading: ""
cta_label: ""
cta_placeholder: ""
note: ""
```

---

## 8. Images, videos, and media

### Page bundles

Every image and video lives **inside its page's directory**, not in a shared `images/` folder.

```
content/use-cases/email-automation/
  index.md           ← the page
  hero.jpg           ← hero image (auto-detected)
  screenshot.png     ← referenced by sections as src: "screenshot.png"
  demo.mp4           ← referenced by video section
```

### Auto-detected images

| Filename pattern | Auto-detected by |
|-----------------|-----------------|
| `hero.jpg`, `hero.png`, `hero.webp` | `hero` section type |
| `cover.jpg`, `cover.png` | Blog template |

### OG / social sharing image

The first entry in the `images:` front matter array becomes the Open Graph image (shown when the page is shared on Twitter, Slack, etc.):

```yaml
images: ["hero.jpg"]   # This file must exist in the page bundle
```

### Image sizing recommendations

| Use | Recommended size | Notes |
|-----|-----------------|-------|
| Hero / Cover | 1200x630px | 1.91:1 ratio, also used as OG image |
| Screenshots | 1200px wide | Height flexible, will scale down |
| Testimonial avatar | 200x200px | Displayed as 48x48 circle |
| Video poster | 1200x675px | 16:9 ratio |

### Supported formats
- Images: `.jpg`, `.png`, `.webp`, `.svg`
- Videos: `.mp4`

---

## 9. Cross-linking between pages

### Linking to related pages

Use the directory name (slug) in `related_use_cases` and `related_blog_posts`:

```yaml
related_use_cases: ["email-automation", "code-review"]
related_blog_posts: ["security-guide"]
```

Hugo resolves these slugs to full URLs automatically. The template renders linked pages as a card grid with images and descriptions.

### Tags

Tags create automatic tag pages at `/tags/tag-name/`:

```yaml
tags: ["email", "productivity", "automation"]
```

The tag name is URL-ified: `"AI Agents"` becomes `/tags/ai-agents/`.

---

## 10. Content writing guidelines

### Voice and tone
- Write in **second person** ("you", "your") for direct engagement
- Lead with the **problem**, then the solution
- Be specific — include **numbers and metrics** wherever possible
- Avoid jargon. If you must use a technical term, explain it briefly

### SEO basics
- **Title:** Under 70 characters. Front-load the key phrase
- **Description:** Under 160 characters. This appears in Google results and social cards
- **Tags:** 2-5 relevant tags per page
- **Slug (directory name):** URL-friendly, descriptive, lowercase, hyphens only

### Markdown body
- Use `##` headings (H2) for main sections within the body — the page title is already H1
- Keep paragraphs short (2-4 sentences)
- Use bold (`**text**`) sparingly for emphasis
- Bullet lists for scannable information
- No raw HTML (Hugo blocks it with `unsafe = false`)

### Front matter YAML
- Strings with special characters need quotes: `title: "LikeClaw vs OpenClaw: What's Different?"`
- Arrays use either inline `["a", "b"]` or block format with `- a` on separate lines
- Booleans: `true` / `false` (lowercase, no quotes)
- Dates: `2026-02-01` (YYYY-MM-DD)

---

## 11. Rules and boundaries

### Allowed
- Create/edit `.md` files in `content/`
- Create/edit `.yaml` files in `data/`
- Add images and videos inside page bundle directories

### Forbidden
- Create files outside `content/` or `data/`
- Modify `.claude/`, `.github/`, or root files
- Use raw HTML in markdown
- Change field names in existing `data/*.yaml` files (templates depend on exact names)
- Delete or rename existing data files
- Create Hugo templates, partials, or shortcodes (these live in the main repo)

---

## 12. Content generation checklist

Use this checklist every time you create a page. Every item is mandatory unless marked optional.

### Pre-writing (before creating the file)

- [ ] **Read product context**: Load `.claude/product-marketing-context.md` — use exact product facts, personas, objections, proof points
- [ ] **Read marketing research**: Check `marketing/` directory for relevant data — `competitive-analysis.md`, `research-openclaw.md`, `research-market-landscape.md`, `gtm-strategy.md`, `landing-page-copy.md`
- [ ] **Identify primary persona**: Which of the 4 personas is this page for? (OpenClaw Refugee, AI-Curious Developer, Non-Technical Founder, Team Lead)
- [ ] **Identify primary keyword**: One main keyword/phrase this page targets
- [ ] **Identify 2-3 secondary keywords**: Related terms to weave into headings and body
- [ ] **Check cross-link plan**: Know which other pages will link TO this page and which pages this page links TO (see cross-link map below)
- [ ] **Determine content type**: Searchable (SEO), shareable (social/HN), or both

### Product knowledge integration (makes content trustworthy)

Every page MUST reference specific, sourced product facts. Pull from this verified fact bank:

**Security facts (source: Snyk, Kaspersky, Cisco, Wiz, Bitsight):**
- 341+ malicious skills found on ClawHub marketplace
- 36% of ClawHub skills contain prompt injection (Snyk)
- 335 of 341 malicious skills installed macOS stealer malware (Atomic Stealer/AMOS)
- Plaintext API keys stored in `~/.clawdbot`
- One-click RCE vulnerability documented
- Organizations warning: Kaspersky, Cisco, Snyk, Wiz, Bitsight
- XDA-Developers headline: "Please stop using OpenClaw"
- Computerworld: "A security nightmare"
- Gary Marcus: "A disaster waiting to happen"

**Cost facts (source: user reports, Federico Viticci, Arsturn research):**
- OpenClaw users spend $50-750/month with no cost controls
- One documented case: $3,600/month (Federico Viticci, 180M tokens)
- Average professional spends $133/month on AI subscriptions
- 42% of AI subscription spending is wasted
- 51% have canceled an AI subscription due to cost
- LikeClaw tiers: Free ($0) / Pro ($15-20/mo) / Power ($40/mo) / Team ($25/seat/mo)

**Setup facts (source: user reports, HN/Reddit threads):**
- OpenClaw: 3+ days typical setup time
- LikeClaw: 30 seconds from signup to first task
- User quote: "I spent three days configuring Moltbot and lost $50 in tokens"
- User quote: "Simpler alternatives cover 99% of what they actually need"

**Product facts:**
- E2B sandboxed execution (isolated container, created per task, destroyed after)
- 100+ AI models: Claude, GPT-4, Gemini, DeepSeek
- Vetted skills marketplace with mandatory security review
- BYOK support on Power plan (zero markup on API calls)
- Persistent workspaces with encrypted file storage
- Background task execution
- Multi-tenant team features with SSO

**Market facts (source: Gartner, growth studies):**
- Market: $3.35B (2025) → $21.11B (2030) at 44.5% CAGR
- Gartner: 40% of enterprise apps will embed AI agents by end 2026
- OpenClaw: 145-157K GitHub stars in 10 weeks, 5 name changes in 3 months
- Founder Peter Steinberger: "I ship code I don't read" (Pragmatic Engineer interview)

**Rule: Every competitive claim must cite one of these sources. No unsourced stats.**

### Brand voice compliance

- [ ] **Tone**: Confident, direct, slightly irreverent. Engineer who's been through it
- [ ] **Person**: Second person ("you", "your")
- [ ] **Structure**: Short sentences. Specific claims. No fluff
- [ ] **Humor**: Dry and factual only. "0 malware. That's the feature." Not forced jokes
- [ ] **Positioning**: Praise OpenClaw's vision, critique execution. Never bash directly
- [ ] **Words to USE**: sandboxed, zero-setup, predictable, vetted, secure, instant, cloud-native, multi-model, BYOK
- [ ] **Words to AVOID**: revolutionary, disruptive, game-changing, AI-powered, innovative, cutting-edge, next-generation, leverage, synergy
- [ ] **No exclamation points** anywhere on the site
- [ ] **No emojis** in content (OK in data cards icon field only)

### SEO requirements

- [ ] **Title**: Under 70 characters, front-loaded with primary keyword
- [ ] **Description**: Under 160 characters, includes primary keyword, compelling for clicks
- [ ] **Slug**: URL-friendly, descriptive, lowercase, hyphens only, includes keyword
- [ ] **Tags**: 2-5 relevant tags per page
- [ ] **Primary keyword** appears in: title, description, first paragraph, at least one H2
- [ ] **Secondary keywords** appear in: other H2s, body paragraphs
- [ ] **H2 headings** mirror search patterns where possible ("How to...", "What is...", "Why...")

### Cross-linking requirements

- [ ] **`related_use_cases`**: List 1-3 related use case slugs
- [ ] **`related_blog_posts`**: List 1-2 related blog post slugs
- [ ] **In-body links**: Mention and link to at least 1 other page naturally in the markdown body
- [ ] **Consistent tagging**: Use shared tags to create automatic tag page clusters

### Section structure quality

- [ ] **Start with `hero`**: Every composable page starts with hero
- [ ] **End with `cta`**: Every page ends with a call-to-action (override defaults if page-specific CTA is stronger)
- [ ] **Include proof points**: At least one of `metrics`, `comparison_table`, or `before_after` per page — data builds trust
- [ ] **Include `faq`**: 3-5 questions per page — captures "People Also Ask" searches
- [ ] **Place `content` intentionally**: Put the markdown body where it fits the narrative arc, not always first
- [ ] **4-8 sections per page**: Enough depth without overwhelming. Use the recipes as starting points

### Content body quality

- [ ] **Lead with the problem**: First paragraph states the pain point, not the product
- [ ] **Specific over general**: "35 hours/month" not "saves time", "$50-750/mo" not "expensive"
- [ ] **Short paragraphs**: 2-4 sentences max
- [ ] **H2 headings**: Every 2-3 paragraphs for scannability
- [ ] **Bold sparingly**: Only for emphasis, not decoration
- [ ] **No raw HTML**: Hugo blocks it
- [ ] **At least 300 words** in the markdown body for SEO

### Post-writing validation

- [ ] **Fact check**: Every stat, quote, and competitive claim maps to a source in the fact bank above
- [ ] **Cross-links work**: All slugs in `related_use_cases` and `related_blog_posts` are real pages (or will be created)
- [ ] **Front matter valid**: YAML parses correctly, all required fields present, dates in YYYY-MM-DD
- [ ] **Page bundle complete**: `index.md` is in the right directory under `content/`
- [ ] **No orphan pages**: Every page links to at least one other page and is linked from at least one other page
- [ ] **Draft status correct**: Set `draft: true` until ready to publish

---

## 13. Cross-link map (content interconnection plan)

Plan all cross-references BEFORE writing content. Every page should link to 2-4 others.

### Comparison pages link to:
- Related use cases (show what you can DO after switching)
- Blog posts that expand on specific comparison dimensions
- Other comparison pages ("Also see: LikeClaw vs ChatGPT")

### Blog posts link to:
- Comparison pages (for readers ready to evaluate)
- Use cases (for readers ready to try)
- Other blog posts in the same pillar

### Use case pages link to:
- Other use cases ("Related workflows")
- Blog posts that provide context/depth
- Comparison pages (for visitors who came from competitor searches)

### Industry pages link to:
- Use cases relevant to that industry
- Blog posts about industry-specific problems

### Tag clusters (shared tags create automatic connections):
- `security` — comparison pages + security blog posts
- `automation` — all use cases + automation blog posts
- `pricing` — cost blog posts + comparison pages
- `ai-agents` — everything
- `openclaw` — comparison + migration + security blog posts
- `productivity` — use cases + workflow blog posts
- `multi-model` — BYOK blog posts + use cases
- `setup` — onboarding blog posts + use cases
