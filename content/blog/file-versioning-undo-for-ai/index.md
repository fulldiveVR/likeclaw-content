---
title: "Undo for AI: Why We Built File Versioning"
description: "AI agents create and modify files constantly. File versioning lets you roll back any change — because even smart agents make mistakes."
date: 2026-01-31
draft: true
images: ["cover.jpg"]
tags: ["building-in-public", "ai-agents", "security"]
categories: ["blog"]
author: "Team LikeClaw"
reading_time: 0
related_use_cases: []
related_blog_posts: ["the-sandbox-bet", "teaching-ai-to-schedule-itself"]
sections:
  - type: hero
  - type: metrics
    headline: "Every file change, preserved"
    items:
      - label: "Versions kept per file"
        value: "All"
      - label: "Time to restore"
        value: "<1s"
      - label: "Files lost to bad AI edits"
        value: "0"
  - type: content
  - type: before_after
    before:
      summary: "Files without versioning"
      items:
        - "AI overwrites your document with a rewrite"
        - "You liked the previous version better — too late"
        - "Background task modifies files while you sleep"
        - "No way to see what changed or when"
    after:
      summary: "Files with versioning"
      items:
        - "Every save creates a snapshot"
        - "Browse version history, see exactly what changed"
        - "One-click restore to any previous version"
        - "Background task results can be rolled back"
  - type: faq
    heading: "Questions about file versioning"
    items:
      - question: "How many versions are stored per file?"
        answer: "All of them. Every save — whether by you or by an AI agent — creates a version snapshot. You can browse the full history and restore any version."
      - question: "Does versioning slow things down?"
        answer: "No. Snapshots are taken asynchronously. The save completes immediately; the version snapshot happens in the background. Users don't experience any delay."
      - question: "Can I see what an AI agent changed in a file?"
        answer: "Yes. Each version has a timestamp and source (user upload, AI modification, background task). You can compare any two versions to see exactly what changed."
  - type: cta
    heading: "AI that respects your work"
    subheading: "Every change tracked. Every version preserved. Always."
---

## The problem with giving AI a pen

Here's something nobody tells you about autonomous AI agents: they're prolific writers with no concept of "are you sure?"

An AI agent asked to "improve this document" will rewrite the entire thing. An agent asked to "clean up this code" will restructure every file it touches. An agent running a background task will create, modify, and delete files without asking permission — because you told it to run autonomously.

Most of the time, the results are good. But "most of the time" isn't good enough when the alternative is losing work you can't get back.

That's why we built file versioning. Every change to every file in every workspace is preserved. Every version can be browsed, compared, and restored with one click.

It's Ctrl+Z for AI.

## February 10, 2026: the commit that changed everything

The commit message reads: "feat: add VFS file versioning with history, restore, and task rollback."

Behind that message is a system that fundamentally changed the relationship between users and their AI agents. Before versioning, giving an AI agent write access to your files required trust. After versioning, it requires nothing — because any change can be undone.

This matters more than you might think.

## Why AI agents need version control

Human file editing is deliberate. You open a file, make changes, save. If you don't like the result, you undo. The cognitive loop is tight: change, evaluate, keep or revert.

AI agent file editing is different. The agent might modify five files in one task. It might run a background job that touches files while you're asleep. It might interpret "update the report" as "rewrite the report from scratch."

Without versioning, every AI file operation is a one-way door. The original is gone. If you don't like the result, you have to manually reconstruct what was there before — assuming you remember.

With versioning, every AI file operation is reversible. The original is preserved. If you don't like the result, you click "restore" and it's back in under a second.

## How it works

**Automatic snapshots.** Every time a file is saved — by you, by an AI agent, by a background task, by a file upload — the previous version is automatically snapshotted. No manual action required. No "remember to commit" step. Every save creates history.

**Version history browser.** Open any file and view its complete history. Every version has a timestamp and context: who changed it (user vs. agent vs. background task), when, and from which session. You can see the full timeline of a file's evolution.

**One-click restore.** Find the version you want. Click restore. The file reverts immediately. The restore itself creates a new version (the current state before restore is preserved), so restoring is also reversible.

**Task rollback.** This is the feature we're most proud of. When a background task modifies files, all those modifications are tagged with the task ID. If the task produced bad results, you can roll back all files it touched to their pre-task state with a single action. Not file by file — all at once.

## The implementation detail that matters

Snapshots are taken using a decorator pattern. The storage provider is wrapped with a `VersionedStorageProvider` that intercepts every write operation and creates a snapshot before the write completes.

This means versioning is invisible to the rest of the system. The AI agent doesn't know files are being versioned. The upload endpoint doesn't know files are being versioned. The background task engine doesn't know files are being versioned. They all just write files normally, and the versioning layer captures everything.

This was a deliberate design choice. We didn't want versioning to be a feature that developers had to remember to use. We wanted it to be a property of the file system itself. Every file is versioned. Always. No opt-in required.

## The trust equation

Before versioning, there was an implicit trust equation every time a user ran an AI agent:

*Is the benefit of this task worth the risk of the agent messing up my files?*

For important files — a carefully written report, a working codebase, a curated dataset — the answer was often "no." Users would copy their files to a separate folder before running an agent. Or they'd avoid giving the agent write access at all. Or they'd watch every file operation in real-time, defeating the purpose of autonomous execution.

Versioning eliminates that equation. The risk of an agent messing up files is zero, because any change can be reversed instantly. Users don't need to copy files before running tasks. They don't need to watch the agent work. They just let it run, review the results later, and roll back anything that isn't right.

This shifts the relationship from "careful delegation" to "confident delegation." Run the task. Check the results. Keep what's good. Revert what's not. It takes ten seconds instead of ten minutes of pre-task preparation.

## The broader lesson

AI agents are powerful. They're also imperfect. The solution isn't to make them perfect — that's an impossible standard. The solution is to make their imperfections reversible.

File versioning is one instance of a broader principle: **build safety nets, not guardrails.** Guardrails prevent the AI from acting. Safety nets let the AI act freely while ensuring that mistakes can be corrected.

Sandboxed execution is a safety net (contains damage). File versioning is a safety net (preserves previous state). Event logging is a safety net (creates audit trails). Each one lets the AI be more autonomous by making autonomy less risky.

The AI agents on LikeClaw are getting better every week. But they'll never be perfect. And that's fine — because with versioning, they don't have to be.
