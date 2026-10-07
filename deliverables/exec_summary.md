# Exec summary: Durable Feed Preferences for Threads

**Ask:** Approve a 4-week A/B test of durable feed preferences in Threads' five Your Algo markets.

## Problem

Users can't make lasting changes to their Threads feed. Feed relevance is the most common complaint in public evidence: **28% of 60 coded items and 36% of non-bug complaints**, appearing every year from 2023 to 2026 and across forums, press and creator blogs. Meta's 2026 controls, Dear Algo and Your Algo, expire after **1 to 7 days**, so users repeat the same requests and rejected content returns.

## Why it matters

- **Scale:** Threads reported **500M monthly users** in June 2026.
- **Headroom:** about **38%** of monthly users are active on a given day (150M daily vs 400M monthly in late 2025).
- **Daily use:** more consistently relevant sessions are a direct lever on how often people come back.
- **Proven demand:** the Dear Algo feature started as a user trend before Meta turned it into a feature.

## Proposal

Add **"Until I change it"** to existing feed controls, prompt users who repeat a request to keep it, and give them an **Interests page** to review and undo preferences. Temporary controls stay unchanged.

## How we'll know

| | |
|---|---|
| **North Star** | Weekly Satisfied Feed Users: users who rate a session worth their time in an in-feed survey |
| **Leading signals** | Repeat-request rate down, "not interested" actions down, D28 retention up |
| **Guardrails** | Time spent, topic diversity, creator reach, integrity reports, ad impressions, latency |
| **Test** | User-level 50/50 split, about 780K users per arm, 4 weeks |

## Cost and risk

- **Effort:** about 4 person-months; it builds on existing controls and ranking inputs.
- **Main risks:** filter bubbles and creator reach. Both have guardrails that block launch if breached.
- **First step:** confirm in logs that users repeat the same request within 14 days. If they don't, stop here.

## Evidence limits

The evidence is public data only: forums, press and blogs, with AI-assisted coding pending a human spot-check. No interviews or app store reviews yet. Both are next and would test whether the pattern holds more broadly.
