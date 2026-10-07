# Threads product case study

A discovery-led product case for Threads (Meta): find one evidenced user problem, prioritize solutions, and write the PRD to ship the best one.

| | |
|---|---|
| **Evidence** | 8 to 10 user interviews plus 150 coded App Store and Google Play reviews |
| **Method** | One shared codebook for both sources, so every claim is backed by a review share and an interview count |
| **Bar for a problem** | Raised unprompted in 30%+ of interviews **and** 10%+ of reviews |
| **Deliverables** | Discovery synthesis, PRD, one-page exec summary |

## Status

| Step | Status | File |
|---|---|---|
| Research plan and hypotheses | Done | [`discovery/01_research_plan.md`](discovery/01_research_plan.md) |
| Screener | Done | [`discovery/02_screener.md`](discovery/02_screener.md) |
| Interview guide (45 min) | Done | [`discovery/03_interview_guide.md`](discovery/03_interview_guide.md) |
| Review codebook | Done | [`reviews/codebook.md`](reviews/codebook.md) |
| Review pull and sampling script | Done | [`reviews/fetch_reviews.py`](reviews/fetch_reviews.py) |
| Review analysis and triangulation script | Done | [`reviews/analyze_reviews.py`](reviews/analyze_reviews.py) |
| Code 150 reviews | To do | `reviews/review_coding_sheet.csv` |
| Interviews | To do | [`synthesis/interview_tracker.csv`](synthesis/interview_tracker.csv) |
| Discovery synthesis | Next | `deliverables/discovery_synthesis.md` |
| PRD | Next | `deliverables/prd.md` |
| One-page exec summary | Next | `deliverables/exec_summary.md` |

## How the evidence flows

```
App Store + Google Play --fetch_reviews.py--> 150-review sample --code with codebook.md--> review_coding_sheet.csv --+
                                                                                                                    +--> analyze_reviews.py --> review_analysis.md
8 to 10 interviews --interview_guide.md--> notes --tag with the same codes--> interview_tracker.csv ----------------+       (theme shares + triangulation)
                                                                                                                                    |
                                                                          problem statement -> solutions (impact vs effort) -> PRD -> exec summary
```

## Run the review analysis

```bash
pip install -r requirements.txt
python reviews/fetch_reviews.py          # pulls recent reviews, writes a 150-review coding sheet
# code the sheet using reviews/codebook.md
python reviews/analyze_reviews.py        # writes reviews/review_analysis.md
```

Reviewer names are never stored. Interview participants appear only as P01 to P10.

## What the PRD will cover

Problem, goals and non-goals, personas from interview segments, user stories, a North Star metric with input metrics, an A/B test design with guardrail metrics and sample size, and a phased rollout with go and no-go criteria.

## Disclaimer

Independent student project. Not affiliated with or endorsed by Meta. Uses only public app store reviews and interviews with consenting participants.
