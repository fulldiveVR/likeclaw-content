# LikeClaw Content Repo — AI Rules

## Boundary
You operate ONLY in this repo. You cannot access templates, CSS, or site config. The main repo (`fulldiveVR/aiwize-com`) controls all design and deployment.

## Allowed actions
- Create/edit `.md` files in `content/`
- Create/edit `.yaml` files in `data/`
- Add images (`.jpg`, `.png`, `.webp`, `.svg`) and videos (`.mp4`) inside page bundle directories

## Forbidden actions
- Create files outside `content/`, `data/`
- Modify `.claude/`, `.github/`, or root files (`.gitignore`, `README.md`)
- Use raw HTML in markdown (Hugo blocks it: `unsafe = false`)
- Change field names in existing `data/*.yaml` files (templates depend on them)
- Delete or rename existing data files
- Create Hugo templates, partials, or shortcodes

---

## Creating a new use case page

1. Create directory: `content/use-cases/my-use-case-slug/`
2. Create `index.md` with required front matter (see schema below)
3. Add `hero.jpg` (1200x630 recommended, also used as OG image)
4. Set `draft: false` when ready to publish
5. Set `related_use_cases` to link to other use case slugs

## Creating a new blog post

1. Create directory: `content/blog/my-post-slug/`
2. Create `index.md` with blog front matter
3. Add `cover.jpg` for the blog card and OG image
4. Set `draft: false` when ready to publish

## Creating a comparison page

1. Create directory: `content/comparisons/likeclaw-vs-competitor/`
2. Create `index.md` with comparison front matter
3. Fill in `comparison_rows` with feature-by-feature breakdown
4. Set `draft: false` when ready to publish

## Creating an industry page

1. Create directory: `content/industries/industry-slug/`
2. Create `index.md` with industry front matter
3. Link to relevant use cases via `related_use_cases`
4. Set `draft: false` when ready to publish

---

## Page bundle rules
- Each page = a directory with `index.md` inside
- Images/videos go IN the page directory (not in a shared folder)
- First image in `images:` front matter array = OG image
- Common file names: `hero.jpg`, `cover.jpg`, `before-after.png`, `demo.mp4`

---

## Front matter schemas

### Use Case (`content/use-cases/*/index.md`)
```yaml
---
title: ""                        # Required
description: ""                  # Required, used in cards and meta
date: 2026-01-01                # Required
draft: true                      # Set false to publish
images: ["hero.jpg"]            # First = OG image (from page bundle)
tags: []                         # e.g. ["productivity", "email"]
categories: ["use-cases"]       # Always "use-cases"
persona: ""                      # e.g. "Developer @ SaaS Startup"
industry: ""                     # e.g. "saas"
difficulty: "beginner"           # beginner | intermediate | advanced
before:
  summary: ""
  pain_points: [""]
after:
  summary: ""
  outcomes: [""]
roi:
  headline: ""                   # e.g. "35 hours/month saved"
  metrics:
    - label: ""
      value: ""
related_use_cases: []            # Slugs of related use case pages
related_blog_posts: []           # Slugs of related blog posts
implementation:
  integrations: []
  steps: [""]
---
```

### Blog Post (`content/blog/*/index.md`)
```yaml
---
title: ""
description: ""
date: 2026-01-01
draft: true
images: ["cover.jpg"]
tags: []
categories: ["blog"]
author: ""
reading_time: 0                  # Minutes. 0 = auto-calculated by template
related_use_cases: []
---
```

### Comparison (`content/comparisons/*/index.md`)
```yaml
---
title: "LikeClaw vs CompetitorName"
description: ""
date: 2026-01-01
draft: true
images: ["og.png"]
tags: ["comparison"]
competitor: "CompetitorName"
competitor_url: ""
verdict: "LikeClaw"              # Who wins overall
comparison_rows:
  - feature: ""
    us: ""
    them: ""
    winner: "us"                 # us | them | tie
related_use_cases: []
---
```

### Industry (`content/industries/*/index.md`)
```yaml
---
title: "LikeClaw for IndustryName"
description: ""
date: 2026-01-01
draft: true
images: ["hero.jpg"]
tags: []
industry_name: "IndustryName"
target_roles: []                 # e.g. ["CTO", "Developer"]
related_use_cases: []
---
```

---

## Data file schemas

### `data/hero.yaml`
```yaml
badge: ""            # Badge text above headline
headline: ""         # Main H1 (supports &nbsp;)
subheadline: ""      # Supporting paragraph
cta_label: ""        # Button text
cta_placeholder: ""  # Email input placeholder
cta_subtext: ""      # Text below CTA (supports &middot;)
success_title: ""    # Post-signup heading
success_text: ""     # Post-signup paragraph
product_visual_label: ""  # Placeholder label
product_visual_hint: ""   # Placeholder hint
```

### `data/problem.yaml`
```yaml
heading: ""          # Section heading
subheading: ""       # Section subheading
cards:               # Exactly 3 cards
  - icon: ""         # clock | lock | dollar
    title: ""
    description: ""
```

### `data/solution.yaml`
```yaml
heading: ""
paragraphs: [""]     # Array of paragraphs
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
  items: [""]        # Bullet points
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
    highlights: ["brand", "default", "default"]  # brand | error | success | muted | default
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

### `data/stats.yaml`
Array of stat items:
```yaml
- value: ""
  label: ""
  source: ""
```

### `data/cta.yaml`
```yaml
heading: ""
subheading: ""
cta_label: ""
cta_placeholder: ""
note: ""
```

---

## Cross-linking
- Use slug names (directory names) in `related_use_cases`, `related_blog_posts`
- Hugo resolves these to full URLs automatically
- Tags create automatic topic pages at `/tags/[tag-name]/`

## Content guidelines
- Write in second person ("you") for direct engagement
- Lead with the problem, then the solution
- Include specific numbers and metrics wherever possible
- Keep titles under 70 characters for SEO
- Keep meta descriptions under 160 characters
