"""Theme analysis of coded public evidence.

    python research/analyze_public.py

Reads research/public_evidence.csv, writes research/public_evidence_analysis.md.
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent


def pct(x: float) -> str:
    return f"{x:.0%}"


def date_range(dates: pd.Series) -> str:
    known = sorted(d for d in dates if d != "undated")
    if not known:
        return "undated"
    rng = known[0] if known[0] == known[-1] else f"{known[0]} to {known[-1]}"
    return rng + (" (+ undated)" if len(known) < len(dates) else "")


def main() -> None:
    df = pd.read_csv(HERE / "public_evidence.csv", dtype=str, keep_default_na=False)
    n = len(df)
    neg = df[df["sentiment"].isin(["negative", "mixed"])]
    nonbug = neg[neg["primary_theme"] != "BUGS_PERFORMANCE"]
    sources = df["source"].nunique()

    any_mention = lambda t: ((df["primary_theme"] == t) | (df["secondary_theme"] == t)).sum()  # noqa: E731
    by_type = df.groupby("source_type")
    themes = df["primary_theme"].value_counts()

    L = ["# Public evidence analysis", "",
         f"**{n} evidence items** from {sources} public sources, dated 2023 to 2026. "
         f"{len(neg)} items ({pct(len(neg) / n)}) are negative or mixed.", "",
         "| Theme | Primary (n) | Share of all | Share of negative, excluding bugs | Any mention | Source types | Date range |",
         "|---|---|---|---|---|---|---|"]
    for t, c in themes.items():
        sub = df[df["primary_theme"] == t]
        share_nb = (nonbug["primary_theme"] == t).mean() if t != "BUGS_PERFORMANCE" else float("nan")
        L.append(f"| {t} | {c} | {pct(c / n)} | {'n/a' if pd.isna(share_nb) else pct(share_nb)} | {any_mention(t)} | "
                 f"{sub['source_type'].nunique()} | {date_range(sub['date'])} |")
    L += ["", "## Theme by source type", "",
          "| Source type | n | Top theme | Top theme share |", "|---|---|---|---|"]
    for st, g in by_type:
        top = g["primary_theme"].value_counts()
        L.append(f"| {st} | {len(g)} | {top.index[0]} | {pct(top.iloc[0] / len(g))} |")
    L += ["", "Bugs are concentrated in the help forum, which people visit when something breaks. "
          "The share of negative items excluding bugs is the fairer view of product problems.", ""]
    (HERE / "public_evidence_analysis.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
