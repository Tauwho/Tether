# YouTube upload: Tether demo

Upload file: `video/Tether Demo v2.mp4` (3:25, 1080p30). Visibility **Public**. Not made for
kids. Category: Science & Technology. Captions: upload `Tether-Demo.en.srt` as English
(Subtitles → Add language → English → Upload file → With timing).

## Title (100 characters max)

Tether: keep Jira tickets consistent with your Confluence decisions | Codegeist 2026

## Description (paste everything between the lines)

---
Tether is a Forge app for Jira and Confluence. It checks a Jira ticket's technical
requirements against the engineering decisions (ADRs) your team already recorded in
Confluence, and shows the exact evidence: the ticket sentence, the decision sentence, and a
link to the page.

Four outcomes: Conflict, Needs review, No conflict found, Insufficient evidence. Interval
maths, units, attempts-versus-retries and supersession are handled in code. The language
model extracts requirements and constraints, with a semantic fallback when the deterministic
rules cannot decide. Tether never edits the ticket or the decision; a follow-up issue is
created only after you review and confirm it.

The same engine runs in the Jira issue panel, as a Rovo agent and skill, and as MCP tools
for clients such as Claude Code. Decisions linked to a ticket are found through Teamwork
Graph. Everything runs on Forge, and model calls use Forge LLMs.

Chapters
0:00 The problem
0:17 What Tether is
0:31 Setup: install and load demo data
0:48 A conflict, with evidence
1:27 Not every different number is a conflict
1:53 Follow-up: you review, Tether drafts
2:09 When a decision changes
2:24 Rovo agent
2:41 MCP: Claude Code calls Tether
2:57 Teamwork Graph and architecture
3:11 Evaluation

Notes
- All data shown is fictional demo data created by the app's "Load demo data" button.
- 30 of 30 team-written test scenarios passed. This shows the prototype handles the cases
  we designed; it is not a measure of real-world accuracy.
- The MCP segment was recorded on our development site; everything else on a clean site
  installed from our install link.
- Narration uses a synthetic (AI-generated) voice.

Built for Codegeist 2026 (Apps for Software Teams).
Code: https://github.com/dngvmnh/Tether
---

## Tags

Atlassian, Forge, Jira, Confluence, Rovo, MCP, Teamwork Graph, Codegeist, ADR,
architecture decision records, AI

## After upload

1. Paste the YouTube link into `docs/DEVPOST.md` (top, "Links to fill in") and
   `docs/SUBMISSION.md` (checklist).
2. Check that the chapters appear on the progress bar and the captions line up at 0:58
   ("Conflict.") and 2:41 (MCP).
