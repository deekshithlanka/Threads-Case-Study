# Research plan: Threads discovery

> **Update:** the first round used public user research (60 coded items from forums, press and blogs) in place of interviews. Interviews and app store reviews remain planned as the next round. See [`../deliverables/discovery_synthesis.md`](../deliverables/discovery_synthesis.md).

## Goal

Find the single most important problem that keeps people from getting value out of Threads, backed by two independent sources: user interviews and app store reviews.

## Research questions

1. What makes a Threads session feel worth it, and what makes it feel wasted?
2. How do people find accounts, topics and conversations they care about?
3. Why do some people post and others only read? What stops readers from posting?
4. Why do people who tried Threads stop opening it?
5. When people choose between Threads and other text-based apps, what decides it?

## Hypotheses to test (not conclusions)

Each one is a guess to confirm or reject. The interview guide does not mention any of them directly.

| ID | Hypothesis | Evidence that would support it | Evidence that would reject it |
|---|---|---|---|
| H1 | The main feed shows too much content people do not care about, so sessions feel low value. | Unprompted complaints about feed content; reviews coded FEED_RELEVANCE are a top theme among 1 to 2 star reviews. | Participants describe the feed as mostly relevant; theme is rare in reviews. |
| H2 | People struggle to find accounts and topics that match their interests. | Participants describe giving up on finding people; DISCOVERY theme in reviews. | Participants find people easily through Instagram or search. |
| H3 | Posters stop posting when they get little response. | Posters link reduced posting to low engagement; REACH theme in reviews. | Posting frequency is driven by time or topic, not response. |
| H4 | Lapsed users left because their community lives elsewhere. | Lapsed participants name another app where "their people" are. | Lapsed participants cite product problems instead. |

## Sources

| Source | Size | What it is good for | Main bias |
|---|---|---|---|
| User interviews | 8 to 10 people, 45 minutes each | Why people behave as they do; stories from real sessions | Small sample; recruited from my network |
| App store reviews | 150 coded (iOS and Android, last 90 days) | How often each problem shows up; severity | Skews toward strong opinions and recent updates |

A problem is considered evidenced only if it appears in both sources (see triangulation in `../reviews/analyze_reviews.py`).

## Participants

Quotas (see `02_screener.md`):

| Segment | Definition | Target |
|---|---|---|
| Regular posters | Opened Threads in the last 7 days and posted or replied 2+ times in the last 30 days | 3 to 4 |
| Readers | Opened Threads in the last 7 days, posted or replied 0 to 1 times in the last 30 days | 3 |
| Lapsed | Used Threads at least weekly for a month or more, have not opened it in 30+ days | 2 to 3 |

Mix targets across all participants: at least 3 who also use X or Bluesky weekly, at least 2 aged 35+, no more than 3 people from the same school or employer.

## Timeline

| Week | Work |
|---|---|
| 1 | Pull and code 150 reviews; recruit and schedule interviews |
| 2 | Run interviews 1 to 5; log each in `../synthesis/interview_tracker.csv` the same day |
| 3 | Run interviews 6 to 10; run triangulation; write discovery synthesis |
| 4 | Problem statement, solution prioritization, PRD, one-page summary |

## Ethics

Ask for consent to record. Store recordings privately and do not commit them. Use participant IDs (P01 to P10) in every shared file. Do not store app store reviewer names.
