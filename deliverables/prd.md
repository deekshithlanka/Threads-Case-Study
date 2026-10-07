# PRD: Durable Feed Preferences for Threads

| | |
|---|---|
| **Status** | Proposal (portfolio case study, not affiliated with Meta) |
| **Evidence** | [Discovery synthesis](discovery_synthesis.md): 60 coded public items, feature timeline, published usage data |
| **One-line pitch** | Let people make the feed choices they already make with Dear Algo and Your Algo stick, so Threads remembers what they want. |

## 1. Problem

Feed relevance is the most common complaint about Threads in public evidence: 36% of non-bug complaints, every year from 2023 to 2026. Meta's 2026 controls address it, but they are temporary. Dear Algo lasts 3 days and Your Algo 1 to 7 days, so users who want lasting changes must repeat themselves, and content they rejected comes back.

**Key assumption to validate first:** a meaningful share of control users repeat the same request within 14 days. If logs show they rarely repeat, durability is not the gap and this PRD should be dropped.

## 2. Goals and non-goals

**Goals**
1. **More relevant sessions:** raise the share of sessions users rate as worth their time.
2. **Less re-tuning:** reduce how often users repeat the same feed request.
3. **Stay in control:** keep preferences private, visible and easy to undo.

**Non-goals**
- Replacing the ranking model or changing how Following and For You are built.
- Chronological or Following-only defaults (these already exist).
- Content moderation policy. Bait demotion (Solution B) is a separate effort.
- Making preferences permanent by default. Temporary controls stay; durability is opt-in.

## 3. Personas

Built from the segments in the evidence.

| Persona | Who | Need | Evidence |
|---|---|---|---|
| **Reader Riya** | Scrolls For You daily, rarely posts | Stop seeing topics and bait she has rejected | Feed relevance items from forums and press |
| **Creator Carlos** | Posts weekly, grows an audience | Reach people who actually want his topic | Creator reach items (2024 to 2026) |
| **Lapsing Lee** | Used Threads weekly, now monthly | A feed worth opening again | Users citing feed quality as a reason to leave |

## 4. User stories

1. **As Riya,** when I tell Threads I want less of a topic, I can choose "keep this" so it stays until I change it.
2. **As Riya,** I can see every preference I've set in one Interests page and remove any of them in one tap.
3. **As Riya,** if I make the same temporary request twice in 14 days, Threads offers to keep it for me.
4. **As Carlos,** people who chose "more of" my topic see my posts more consistently.
5. **As Lee,** when I return after a while, my saved preferences still shape my feed.
6. **As any user,** my preferences are private and are never shown on my profile.

## 5. Solution

| Component | What it does |
|---|---|
| "Keep this" option | Adds a fourth duration, "Until I change it," to Your Algo and to Dear Algo confirmations |
| Smart prompt | After the second identical request within 14 days, asks "Keep this preference?" |
| Interests page | Settings page listing all active preferences with type, duration, and one-tap remove |
| Ranking input | Saved preferences become a persistent user-level signal, with the same weight as an active Your Algo request |
| Decay safeguard | Saved "less of" preferences never fully block a topic, so major news still surfaces |

## 6. Success metrics

**North Star: Weekly Satisfied Feed Users.** The number of users who rate at least one session that week as worth their time (4 or 5 out of 5) in an in-feed pulse survey. It counts people who got value, not minutes spent.

| Input metric | Definition | Expected direction |
|---|---|---|
| Repeat-request rate | Share of control users repeating the same request within 14 days | Down |
| Saved preference adoption | Share of control users with 1+ saved preference after 28 days | Up |
| Negative feedback rate | "Not interested" and hide actions per 1,000 impressions | Down |
| Preferred-topic share | Share of For You impressions matching a saved "more of" topic | Up |
| D28 retention | Control users active again 28 days later | Up |

**Guardrails** (the launch is blocked if any of these moves past its threshold)

| Guardrail | Threshold |
|---|---|
| Time spent per DAU | Not down more than 1% |
| Topic diversity (distinct topics per user per week) | Not down more than 5%, to avoid filter bubbles |
| Creator unconnected reach, median | Not down more than 3% |
| Integrity reports per 1,000 impressions | No significant increase |
| Ad impressions per DAU | Not down more than 1% |
| Feed load latency, p95 | No regression over 50 ms |

## 7. A/B test design

| Item | Plan |
|---|---|
| **Unit** | User, randomized 50/50 |
| **Population** | Users in Your Algo markets (US, Canada, UK, Australia, New Zealand) who used Dear Algo or Your Algo in the last 30 days |
| **Treatment** | Keep-this option, smart prompt, and Interests page |
| **Control** | Current temporary controls only |
| **Primary metric** | Share of surveyed sessions rated worth your time |
| **Secondary metrics** | Repeat-request rate, negative feedback rate, D28 retention |
| **Sample size** | Assuming a 55% baseline and a 1-point minimum detectable effect at 95% confidence and 80% power: **about 38,900 survey responses per arm**. At an assumed 5% survey response rate, that is **about 780,000 users per arm**, a small slice of eligible users. |
| **Duration** | 4 weeks. Your Algo lasts up to 7 days, so a durability effect needs at least 2 to 3 weeks to appear, and 4 weeks covers weekly cycles and novelty. |
| **Analysis** | Intent-to-treat on all randomized users; CUPED variance reduction using pre-period engagement; guardrails checked weekly |
| **Decision rule** | Ship if the primary metric is significantly positive and no guardrail is breached. Iterate if the primary is flat but repeat requests drop. Stop if any guardrail is breached. |

The 55% baseline and 5% response rate are planning assumptions. Replace them with real values before launch.

## 8. Phased rollout

| Phase | Audience | Length | Go criteria for the next phase |
|---|---|---|---|
| 0. Dogfood | Employees | 2 weeks | No P0 bugs; Interests page usable |
| 1. A/B test | Eligible control users, as above | 4 weeks | Decision rule met |
| 2. Expand | All control users in launch markets | 2 weeks | Guardrails stable at scale |
| 3. Default prompt | All users in launch markets see the smart prompt | 4 weeks | North Star up, no diversity drop |
| 4. International | Remaining markets, by region | Ongoing | Local integrity review complete |

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Filter bubbles | Decay safeguard; topic diversity guardrail |
| Lower reach for some creators | Creator reach guardrail; publish guidance on how preferences affect distribution |
| Users forget saved preferences | Interests page plus a periodic "still want this?" check |
| Durability is not the real gap | Validate the repeat-request assumption in logs before building |
| Privacy concerns | Private by default, never shown publicly, included in data download |

## 10. Open questions

1. Should saved "less of" preferences expire after a long period (for example 6 months) unless confirmed?
2. Do saved preferences apply to Communities feeds, or only to For You?
3. How should a saved preference interact with someone the user follows?
