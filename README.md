# LikeClaw Content

Content repository for [likeclaw.ai](https://likeclaw.ai). This repo contains all marketing copy, blog posts, use cases, comparisons, and data files.

## Structure

```
content/               Markdown content (page bundles)
  _index.md            Homepage meta
  use-cases/           Use case pages
  blog/                Blog posts
  comparisons/         Competitor comparisons
  industries/          Industry-specific pages
data/                  YAML data files for homepage sections
```

## How it works

This repo is a **git submodule** of `fulldiveVR/aiwize-com`. Pushing to `main` here triggers a deploy of the main site via GitHub Actions.

## Adding content

Each page is a **page bundle** — a directory containing `index.md` plus any images/videos:

```
content/use-cases/my-new-use-case/
  index.md        # Page content + front matter
  hero.jpg        # Hero image (also used as OG image)
  demo.mp4        # Optional video
```

See `.claude/CLAUDE.md` for front matter schemas and content guidelines.

## Data files

Homepage sections are driven by YAML data files in `data/`. Edit these to update homepage copy. **Do not rename or delete data files** — the site templates depend on their exact names and field structures.
