# Screener

Send as a short form (Google Forms or similar). About 2 minutes. Use answers to place people in a segment and to fill the quotas in `01_research_plan.md`.

Intro text for the form:

> I'm a student researching how people use text-based social apps. I'm looking for people for a 45-minute video call. Your answers stay private and are only used to choose participants.

## Questions

**S1. Which of these apps have you opened in the last 30 days?** (select all)
Threads / X (Twitter) / Bluesky / Instagram / Reddit / Mastodon / LinkedIn / None of these

- Never used Threads at all (not selected here and answers "never" in S2): **end, thank them**

**S2. When did you last open Threads?**
Today or yesterday / 2 to 7 days ago / 8 to 30 days ago / More than 30 days ago / I have never used Threads

- "Never used": **end**

**S3. (If last opened more than 30 days ago) Before you stopped, how often did you use Threads?**
Daily / A few times a week / About once a week / Less than once a week

- Less than once a week: **end** (not enough experience to talk about)

**S4. In the last 30 days, about how many times did you post or reply on Threads?**
0 / 1 / 2 to 5 / 6 to 20 / More than 20

**S5. How old are you?**
Under 18 / 18 to 24 / 25 to 34 / 35 to 44 / 45 or older

- Under 18: **end** (consent rules)

**S6. Do you work at Meta, or in social media marketing, or in UX research?**
Yes / No

- Yes: **end** (expert bias)

**S7. Are you available for a 45-minute video call in the next 2 weeks? Add your email.**

## Segment logic

| Segment | S2 | S4 |
|---|---|---|
| Regular poster | Today to 7 days ago | 2 or more |
| Reader | Today to 7 days ago | 0 or 1 |
| Lapsed | More than 30 days ago (and S3 weekly or more) | any |

People who last opened Threads 8 to 30 days ago do not fit a segment. Keep them as backups.

## Where to recruit

LinkedIn post, university Slack or Discord groups, friends of friends (not close friends), and relevant subreddits where self-promotion rules allow it. Note the source of every participant in the tracker so you can report recruiting bias.
