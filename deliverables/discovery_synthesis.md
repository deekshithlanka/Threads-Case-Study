# Discovery synthesis: Threads

## TL;DR

- **Problem:** Threads users cannot durably tell the feed what they want. Feed relevance is the most common complaint in the public evidence: **28% of all items and 36% of non-bug complaints**, appearing **every year from 2023 to 2026** and in **all three source types**.
- **Why now:** Meta's newest fixes, Dear Algo and Your Algo, expire after **1 to 7 days**. A user who wants less of a topic has to keep asking.
- **Recommendation:** Make feed preferences durable (Solution A). It ranks first on impact versus effort, builds on controls Meta already shipped, and can be tested in a standard A/B experiment.

## Method

| Source | What | Size | Bias to keep in mind |
|---|---|---|---|
| Public discussions | Forum comments from MetaFilter and a Lemmy thread; posts from the r/ThreadsApp help forum | 49 items | Help forum skews to bugs; forum users skew technical and Meta-skeptical |
| Press, blogs and reviews | Reporting and first-person accounts from readers, creators and businesses | 11 items | Press covers what is newsworthy, which skews to controversy |
| Published data | Meta-reported usage plus Similarweb estimates and the feature timeline | See [published_data.md](../research/published_data.md) | Third-party estimates are approximate |

All 60 items are in [`research/public_evidence.csv`](../research/public_evidence.csv), each with a source link, date, sentiment and theme from the shared [codebook](../reviews/codebook.md). Coding was AI-assisted and is marked for human spot-check. Full tables: [`public_evidence_analysis.md`](../research/public_evidence_analysis.md).

**What this study is not:** it has no interviews or app store reviews yet. Both are planned (see Next steps) and would test whether the pattern holds outside forums and press.

## What the evidence says

| Theme | Share of all items | Share of non-bug complaints | Seen in |
|---|---|---|---|
| **Feed relevance** | **28%** (17) | **36%** | 3 of 3 source types, 2023 to 2026 |
| Bugs and performance | 18% (11) | n/a | Mostly the help forum |
| Moderation | 7% (4) | 9% | 2 source types |
| Privacy and Meta trust | 7% (4) | 9% | 1 source type |
| Instagram coupling | 7% (4) | 9% | 1 source type |
| Creator reach | 5% (3) | 7% | 2023 to 2026, creators and businesses |
| Conversation quality | 3% (2) | 4% | Also a secondary theme in 3 more items |

### Insights

1. **The complaint has changed shape but not gone away.** In 2023 the ask was a Following-only feed. In 2024 and 2025 it was engagement bait and spam in recommendations. In 2026, a commenter welcomed the new private controls but called them overdue. Each fix moved the complaint rather than closing it.
2. **Users already try to teach the feed, and Meta productized that behavior.** The Dear Algo trend started as users joking to the algorithm before it became a feature. That shows strong demand for control.
3. **The controls are temporary by design.** Dear Algo lasts 3 days and Your Algo up to 7. That suits passing interests, such as a sports final, but not lasting dislikes, such as rage bait or a topic someone never wants.
4. **Creators feel the same problem from the other side.** When the feed is unpredictable, creators report low or inconsistent engagement and some leave for platforms where their audience is reachable.
5. **Bugs are real but likely overstated here.** They are 45% of help-forum posts and nearly absent elsewhere, so they reflect where people go when something breaks.

## Problem statement

> Threads users who want to shape their feed have no lasting way to do it. Feed relevance is the most frequent complaint in public evidence (36% of non-bug complaints, 2023 to 2026), and the controls Meta shipped in 2026 expire within 1 to 7 days. As a result, users repeat the same requests, keep seeing content they rejected, and get less value per session. With roughly 38% of monthly users active on a given day, more consistently relevant sessions are a direct lever on daily use.

## Solutions considered

RICE inputs are estimates for prioritization, not measured data. Reach is users per quarter.

| Solution | Reach | Impact (0.25 to 3) | Confidence | Effort (person-months) | RICE |
|---|---|---|---|---|---|
| **A. Durable preferences:** a "keep this" option on Dear Algo and Your Algo, plus an editable Interests page | 15M (assumes 10% of DAU use feed controls) | 2 | 50% | 4 | **3.8** |
| B. Stronger bait demotion using reply-quality signals | 150M | 0.5 (extends work Meta started in 2024) | 50% | 12 | 3.1 |
| C. Following-first feed for a user's first week | 10M new users | 0.5 | 30% | 2 | 0.8 |
| D. In-feed "worth your time?" pulse survey | 150M | 0.25 (measurement, not a fix) | 80% | 1 | 30 |

**D scores highest, but it doesn't solve the problem.** It is cheap instrumentation, so it ships alongside A as the way to measure session quality.

**A is the bet:** it targets the exact gap the evidence points to, reuses controls users already know, and is low risk to test.

## Next steps

1. **App store reviews:** run `reviews/fetch_reviews.py` and code 150 reviews to test whether feed relevance also leads there.
2. **Survey:** a 5-question survey (based on the screener) on how often people re-tune their feed.
3. **Log analysis:** with internal data, measure how often users repeat the same Dear Algo or Your Algo request within 14 days. This is the key assumption behind Solution A.
