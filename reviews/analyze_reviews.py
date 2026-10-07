"""Summarize coded reviews and triangulate them with interview themes.

    python reviews/analyze_reviews.py

Reads:
    reviews/review_coding_sheet.csv      coded reviews
    synthesis/interview_tracker.csv      interview log (optional)
Writes:
    reviews/review_analysis.md
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
THEMES = ["FEED_RELEVANCE", "DISCOVERY", "REACH", "CONVERSATION_QUALITY", "MODERATION",
          "BUGS_PERFORMANCE", "MISSING_FEATURE", "INSTAGRAM_LINK", "ADS", "PRIVACY", "PRAISE", "OTHER"]


def kappa(a: list[str], b: list[str]) -> float:
    labels = sorted(set(a) | set(b))
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(l) / n) * (b.count(l) / n) for l in labels)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def pct(x: float) -> str:
    return f"{x:.0%}"


def review_tables(df: pd.DataFrame) -> tuple[list[str], pd.DataFrame]:
    df = df[df["primary_theme"].fillna("").str.strip() != ""].copy()
    unknown = sorted(set(df["primary_theme"]) - set(THEMES))
    if unknown:
        raise SystemExit(f"Unknown theme codes: {unknown}. Fix them or add them to THEMES and the codebook.")
    df["severity"] = pd.to_numeric(df["severity"], errors="coerce").fillna(0)
    n = len(df)
    low = df[df["rating"] <= 2]

    rows = []
    for t in THEMES:
        primary = df["primary_theme"] == t
        any_mention = primary | (df["secondary_theme"].fillna("") == t)
        if not any_mention.any():
            continue
        rows.append({
            "theme": t,
            "primary_n": int(primary.sum()),
            "share_all": primary.mean(),
            "share_1_2_star": (low["primary_theme"] == t).mean() if len(low) else float("nan"),
            "mentions_any": int(any_mention.sum()),
            "avg_rating": df.loc[primary, "rating"].mean() if primary.any() else float("nan"),
            "churn_signal_n": int((primary & (df["severity"] >= 3)).sum()),
        })
    table = pd.DataFrame(rows).sort_values("primary_n", ascending=False)

    L = ["# App store review analysis", "",
         f"**{n} reviews coded** ({df['source'].value_counts().to_dict()}), "
         f"dates {df['date'].min()} to {df['date'].max()}. "
         f"Average rating {df['rating'].mean():.1f}. {len(low)} reviews ({pct(len(low) / n)}) are 1 or 2 stars.", "",
         "| Theme | Primary (n) | Share of all | Share of 1 to 2 star | Any mention | Avg rating | Says they left or will leave |",
         "|---|---|---|---|---|---|---|"]
    for r in table.itertuples():
        L.append(f"| {r.theme} | {r.primary_n} | {pct(r.share_all)} | {pct(r.share_1_2_star)} | "
                 f"{r.mentions_any} | {r.avg_rating:.1f} | {r.churn_signal_n} |")
    L.append("")

    feats = df.loc[df["primary_theme"] == "MISSING_FEATURE", "feature_requested"].dropna()
    feats = feats[feats.str.strip() != ""].str.lower().str.strip().value_counts().head(8)
    if len(feats):
        L += ["**Most requested features:** " + ", ".join(f"{k} ({v})" for k, v in feats.items()), ""]

    if "coder2_primary_theme" in df and df["coder2_primary_theme"].fillna("").str.strip().ne("").sum() >= 10:
        both = df[df["coder2_primary_theme"].fillna("").str.strip() != ""]
        k = kappa(both["primary_theme"].tolist(), both["coder2_primary_theme"].str.strip().tolist())
        L += [f"**Inter-coder reliability:** Cohen's kappa {k:.2f} on {len(both)} double-coded reviews "
              f"({'acceptable' if k >= 0.6 else 'below 0.6, tighten the codebook'}).", ""]
    else:
        L += ["**Inter-coder reliability:** not yet measured (needs 10+ rows in `coder2_primary_theme`).", ""]

    quotes = df[df["quote_worthy"].fillna("").str.lower() == "yes"]
    if len(quotes):
        L += ["## Candidate quotes (top 3 themes)", ""]
        for t in table["theme"].head(3):
            for q in quotes[quotes["primary_theme"] == t].head(2).itertuples():
                text = str(q.text).replace("\n", " ")
                L.append(f"- **{t}** ({q.rating} star, {q.source}): \"{text[:220]}{'...' if len(text) > 220 else ''}\"")
        L.append("")
    return L, table


def triangulation(table: pd.DataFrame, tracker: Path) -> list[str]:
    if not tracker.exists():
        return []
    iv = pd.read_csv(tracker, dtype=str, keep_default_na=False)
    iv = iv[iv["participant_id"].fillna("").str.strip() != ""]
    if iv.empty:
        return ["## Triangulation", "", "No interviews logged yet.", ""]
    n_iv = len(iv)
    L = ["## Triangulation: reviews vs interviews", "",
         f"{n_iv} interviews logged. Interview counts use unprompted mentions only.", "",
         "| Theme | Share of reviews | Share of 1 to 2 star | Interviews mentioning (unprompted) | Segments | Evidence |",
         "|---|---|---|---|---|---|"]
    review_share = table.set_index("theme")
    for t in THEMES:
        hits = iv[iv["themes_unprompted"].fillna("").str.contains(rf"\b{t}\b")]
        r_all = review_share["share_all"].get(t, 0.0)
        r_low = review_share["share_1_2_star"].get(t, 0.0)
        if not len(hits) and r_all == 0:
            continue
        both = len(hits) >= max(3, round(0.3 * n_iv)) and r_all >= 0.10
        strength = "strong (both sources)" if both else ("one source" if len(hits) or r_all else "none")
        segs = ", ".join(sorted(hits["segment"].dropna().unique())) or "none"
        L.append(f"| {t} | {pct(r_all)} | {pct(r_low)} | {len(hits)} of {n_iv} | {segs} | {strength} |")
    L += ["", "Strong = mentioned unprompted in at least 30% of interviews (minimum 3) and at least 10% of reviews.", ""]
    return L


def main() -> None:
    sheet = HERE / "review_coding_sheet.csv"
    if not sheet.exists():
        raise SystemExit("Run fetch_reviews.py first, then code the sheet.")
    df = pd.read_csv(sheet, dtype=str, keep_default_na=False)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    L, table = review_tables(df)
    L += triangulation(table, ROOT / "synthesis" / "interview_tracker.csv")
    (HERE / "review_analysis.md").write_text("\n".join(L))
    print("Wrote reviews/review_analysis.md")


if __name__ == "__main__":
    main()
