# Devpost "Additional info" form: paste-ready answers (14 Nov 2026)

## Testing instructions

```
You need an Atlassian Cloud site with Jira and Confluence (a free site works) where you are a site admin. Rovo must be available for the agent; everything else works without it. All data is fictional demo data created by the app.

Installation link (Jira + Confluence):
https://developer.atlassian.com/console/install/07520459-db83-4ab5-b000-09c3c8095691?signature=AYABeErpGojCngGAq6cJ4g%2FXv3IAAAADAAdhd3Mta21zAEthcm46YXdzOmttczp1cy13ZXN0LTI6NzA5NTg3ODM1MjQzOmtleS83MDVlZDY3MC1mNTdjLTQxYjUtOWY5Yi1lM2YyZGNjMTQ2ZTcAuAECAQB4CxqLTo9l4lqXuFjNim1xJM%2Bp%2F3TVP9xHS2BrU5DRRucBlx5ejTkNbBe95tlFfOe3pgAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDD1jXdhdP2eLtW0OgAIBEIA7ANwgnVc%2FTPB%2Bap1nqLLr30nZnAi2HB1SnZ3fpRxa%2FcwGLDtXRcRSrwb49CMWCuJNjpTH7rcsvn6TnXYAB2F3cy1rbXMAS2Fybjphd3M6a21zOmV1LXdlc3QtMTo3MDk1ODc4MzUyNDM6a2V5LzQ2MzBjZTZiLTAwYzMtNGRlMi04NzdiLTYyN2UyMDYwZTVjYwC4AQICAHi9bVMAkme4qVQX1fQHo6ePw3H40A7cGfz7yrmSfBWMXgHegWr%2BchkFFstK3R6bBE6mAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM3jpVZRxub7nQFdY5AgEQgDtxW0Kmrfdnl7Eecxa3wn6TB11iD5lPmFqWBbT9MKED3YxdTcR3%2FtUse1zWOjpMtYAhFxVzYHyJgftsoQAHYXdzLWttcwBLYXJuOmF3czprbXM6dXMtZWFzdC0xOjcwOTU4NzgzNTI0MzprZXkvNmMxMjBiYTAtNGNkNS00OTg1LWI4MmUtNDBhMDQ5NTJjYzU3ALgBAgIAeDYASx0XCjkny4iLV6vz%2BKtEGSGT6kdt0QRpkn6D%2FlVEAWXa%2BPYYtb6OpTddjxgBXcMAAAB%2BMHwGCSqGSIb3DQEHBqBvMG0CAQAwaAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAywWezSLKYixJlx8F4CARCAO2Ij6c%2FGVbaylHgdNWmgXMJXdR0XkQVkKOTNNF3Dr90seKCkBZFNZ02qaTh5ShvZOE8z%2B934weF%2FBdrXAgAAAAAMAAAQAAAAAAAAAAAAAAAAAKgoqySX5f31ottWQxNQY83%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAADJZH9UbMLXqOSANS0ZpqiUcdQSiA2PAdVfFBVagEGYmsESqB0RQsXga%2FJEK%2BrpD%2Bamilxv7ZEeEN0n%2FCaQq0kiRsNE%3D&product=jira&product=confluence

1. Install: open the link, choose your site, keep Jira and Confluence ticked, click Install. If one product reports "Installation failed", click Install again.
2. Grant access: in Jira, Settings (gear) > Apps > Tether settings. If asked, click Allow access, then Accept.
3. Load demo data: on the same page click Load demo data and wait about a minute. It creates project PAY (30 issues) and space ENG (10 decision records) and configures Tether. If a project with key PAY already exists, use a fresh site.
4. Run a check: open PAY-1, click the apps button under the title, choose Tether decision check, then Check implementation context. The first check takes about a minute.

Expected results (wording can vary, the outcome should match):
- PAY-1: Conflict, 1 of 2 checked ("exactly 5 times" vs ADR-PAY-001 "no more than 3 times")
- PAY-2: Insufficient evidence, 1 of 2 checked
- PAY-3: Needs review ("exactly 4 attempts": is the first try an attempt?)
- PAY-4: Conflict (cites ADR-PAY-000, superseded by ADR-PAY-001)
- PAY-5: Insufficient evidence (decisions exist, but for another service)
- PAY-13: No conflict found (4 attempts including the first = 3 retries)
- PAY-14: Conflict (15000 ms vs at most 10 s)

5. Follow-up: on PAY-1's conflict click Create clarification issue, edit if you like, confirm. The new issue links to PAY-1 and the decision page.
6. Drift: in Confluence edit and publish ADR-PAY-001, then reopen PAY-1: "A decision used in this check has changed" with Re-check.
7. Rovo agent: Rovo > Agents > Tether, ask "Does PAY-2 conflict with any engineering decision?".
8. MCP (optional): admin.atlassian.com > your site > Connected apps > Tether > Details > Tools, enable "Expose tools to MCP-compatible apps". Add https://mcp.atlassian.com/forge/07520459-db83-4ab5-b000-09c3c8095691 to an MCP client (e.g. claude mcp add --transport http tether <url>), sign in, ask about PAY-1.
9. Evaluation: Tether settings > Run eval runs our 30 scenarios on fixture data (1-3 minutes, then Refresh). It never reads your site's data.

Teamwork Graph is used automatically: PAY-1's panel footer says "1 page(s) linked to PAY-1 in Teamwork Graph".
Step-by-step with screenshots: https://github.com/dngvmnh/Tether#try-it
```

## App ID

```
07520459-db83-4ab5-b000-09c3c8095691
```

(The judging app "Tether". Not the Marketplace copy 9cca0b82-....)

## How the project meets the main technology requirement

```
Tether is built entirely on Forge, with no external services (no egress); the production build is eligible for Runs on Atlassian.

- Forge: Custom UI issue panel and admin page, resolvers that enqueue work, a queue consumer that runs the analysis, Forge storage (KVS) for jobs, reports, cache and settings, product triggers, and Forge LLMs for requirement and constraint extraction.
- Jira: the issue panel reads the work item as the user; Tether creates a clarification issue (only after the user confirms) linked to the ticket and the decision; the demo-data loader creates the PAY project.
- Confluence: decision records (ADRs) are ordinary labelled pages with a Page Properties table; Tether finds them with CQL, drops pages the user cannot read, and flags tickets when a decision page changes.
- Rovo: a Tether agent with three actions and a skill (decision-consistency) that answers "does this ticket conflict with our decisions?" in chat.
- MCP: rovo:mcp exposes check-issue-consistency and find-decisions to external AI clients such as Claude Code.
- Teamwork Graph: a Cypher query follows the work item's links to the Confluence pages they point to, so a decision linked to the ticket is found even without the label.
```

## Category

Apps for Software Teams

## Why this category

```
Tether is for software teams: it keeps Jira tickets consistent with the engineering decisions (ADRs) the team already recorded in Confluence. Conflicts like "retry exactly 5 times" against a decision that allows at most 3 usually surface only in code review or production. Tether catches them on the ticket, before work starts, with the exact quotes from both sides, and it works where engineers already are: the Jira issue panel, Rovo chat and their own AI coding tools over MCP.
```

## Bonus prizes

Select all four if the field allows several: Best Marketplace published app, Best Agents,
Best app with MCP, Best Teamwork Graph integration. If it allows only one: **Best
Marketplace published app** (it has its own URL field).

## Best Marketplace published app: URL

```
https://marketplace.atlassian.com/apps/1533276126
```

Submitted 14 Nov 2026, pending approval: the page may show "not found" until Atlassian
approves it. Replace it with the review ticket link if Atlassian emails one first.
