# Threads product case study

A discovery-led product case for Threads (Meta): find one evidenced user problem, prioritize solutions, and write the PRD to ship the best one.

| | |
|---|---|
| **Problem found** | Users can't make lasting changes to their feed. Feed relevance is **36% of non-bug complaints** across 60 coded public items (2023 to 2026), and Meta's 2026 controls expire in 1 to 7 days. |
| **Proposal** | Durable Feed Preferences: a "keep this" option, a repeat-request prompt, and an Interests page |
| **North Star** | Weekly Satisfied Feed Users |
| **Test** | 50/50 user-level A/B test, about 780K users per arm, 4 weeks, 6 guardrails |
| **Evidence** | 60 public items from 13 sources, coded with one codebook, plus published usage data |

## Read in this order

1. [**Exec summary**](deliverables/exec_summary.md): one page.
2. [**PRD**](deliverables/prd.md): problem, goals and non-goals, personas, user stories, metrics, A/B test, rollout.
3. [**Discovery synthesis**](deliverables/discovery_synthesis.md): evidence, insights, problem statement, RICE prioritization.
4. [**Evidence**](research/public_evidence.csv), [analysis](research/public_evidence_analysis.md), and [published data](research/published_data.md).

## Method

| Step | What | File |
|---|---|---|
| Codebook | 12 themes with include and exclude rules, shared across all sources | [`reviews/codebook.md`](reviews/codebook.md) |
| Public user research | 60 items from forums, a help forum, press, blogs and review sites, each linked and dated | [`research/public_evidence.csv`](research/public_evidence.csv) |
| Theme analysis | Theme shares overall, excluding bugs, and by source type | [`research/analyze_public.py`](research/analyze_public.py) |
| Published data | Meta-reported usage, Similarweb estimates, and a feed-feature timeline | [`research/published_data.md`](research/published_data.md) |
| Prioritization | RICE across 4 solutions, with assumptions stated | [`deliverables/discovery_synthesis.md`](deliverables/discovery_synthesis.md) |

```bash
pip install -r requirements.txt
python research/analyze_public.py     # rebuilds the theme analysis
```

## Next steps

| Step | Status | File |
|---|---|---|
| Code 150 app store reviews | Planned | [`reviews/fetch_reviews.py`](reviews/fetch_reviews.py), [`reviews/analyze_reviews.py`](reviews/analyze_reviews.py) |
| User interviews or survey | Planned | [`discovery/03_interview_guide.md`](discovery/03_interview_guide.md), [`discovery/02_screener.md`](discovery/02_screener.md) |
| Human spot-check of AI-assisted coding | Planned | `coder` column in the evidence file |

## Limitations

Public data only: forums and press skew toward strong opinions, and the help forum skews toward bugs. Coding was AI-assisted and is marked for human spot-check. RICE inputs and A/B test baselines are labeled planning assumptions, not measured data.

## Disclaimer

Independent project. Not affiliated with or endorsed by Meta. Uses only public information.
