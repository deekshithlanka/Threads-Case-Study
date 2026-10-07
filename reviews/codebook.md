# Review codebook

Used for both app store reviews and interview notes, so the two sources can be compared theme by theme.

## How to code

1. Read the full review. Pick **one primary theme**: the problem the reviewer spends the most words on or names as the reason for the rating.
2. Add **one secondary theme** only if a second problem is clearly stated.
3. Set **sentiment**, **severity**, and **user type**.
4. Mark **quote_worthy = yes** if the review states a problem clearly in one or two sentences.
5. **Process:** code the first 30 reviews, then review the codebook. Add a theme only if 3 or more reviews do not fit any existing one. Then freeze the codebook and recode the first 30.
6. **Reliability check:** have a second person code a random 20% (30 reviews) into the `coder2_primary_theme` column. The analysis script reports Cohen's kappa. Aim for 0.6 or higher; if lower, tighten definitions and recode.

## Themes

| Code | Definition | Include | Exclude |
|---|---|---|---|
| FEED_RELEVANCE | The main feed shows content the user does not want or care about | Irrelevant posts, repeated posts, engagement bait, "not seeing people I follow" | Offensive content (CONVERSATION_QUALITY), ads (ADS) |
| DISCOVERY | Hard to find accounts, topics, communities, or posts | Search complaints, can't find people with my interests, topics hard to follow | Feed ranking itself (FEED_RELEVANCE) |
| REACH | The user's own posts get low visibility or engagement | "No one sees my posts," follower growth, views dropped | Not seeing others' posts (FEED_RELEVANCE) |
| CONVERSATION_QUALITY | Replies and discussions are hostile, low quality, or hard to follow | Trolls, rage bait in replies, bots, reply threading confusion | Moderation decisions (MODERATION) |
| MODERATION | Content or account enforcement | Bans, removed posts, shadowban claims, appeals, reporting does nothing | |
| BUGS_PERFORMANCE | The app does not work as expected | Crashes, slow loading, broken notifications, login loops, battery | Missing features (MISSING_FEATURE) |
| MISSING_FEATURE | A feature the reviewer wants that does not exist or that they cannot find | Write the feature in `feature_requested` | Broken existing features (BUGS_PERFORMANCE) |
| INSTAGRAM_LINK | Problems caused by Threads being tied to Instagram | Account deletion, required IG account, cross-posting, IG followers | |
| ADS | Ads frequency, relevance, or format | | |
| PRIVACY | Data collection, tracking, privacy settings | | |
| PRAISE | Positive with no specific problem | "Love it," "better than X" | Positive reviews that also name a problem: code the problem |
| OTHER | Fits nothing above | Write a short note | |

## Other fields

| Field | Values | Rule |
|---|---|---|
| sentiment | negative, mixed, positive | Mixed = names both something liked and a problem |
| severity | 0, 1, 2, 3 | 0 = no problem; 1 = annoyance; 2 = makes the app worse to use; 3 = says they stopped, deleted, or will leave |
| user_type | poster, reader, business, unknown | Only if the review makes it clear; otherwise unknown |
| quote_worthy | yes, no | States a problem clearly in one or two sentences |
| feature_requested | free text | Only for MISSING_FEATURE |

## Interview coding

In `../synthesis/interview_tracker.csv`, list every theme a participant raised **without being prompted** in `themes_unprompted` (semicolon separated, for example `FEED_RELEVANCE;REACH`). Themes raised only after a direct question go in `themes_prompted`. Only unprompted mentions count toward triangulation.
