"""Pull recent Threads reviews from the App Store and Google Play, then draw a
stratified sample into a coding sheet.

    pip install pandas google-play-scraper
    python reviews/fetch_reviews.py                 # pull + sample 150
    python reviews/fetch_reviews.py --sample 200 --days 60

Outputs:
    reviews/raw_reviews.csv          everything pulled (no reviewer names)
    reviews/review_coding_sheet.csv  the sample, with empty coding columns

Sources:
    iOS: Apple's public customer reviews RSS feed (up to 10 pages of 50 per country)
    Android: the google-play-scraper package
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
IOS_APP_ID = "6446901002"                # apps.apple.com/us/app/threads/id6446901002
ANDROID_PACKAGE = "com.instagram.barcelona"

CODING_COLUMNS = [
    "primary_theme", "secondary_theme", "sentiment", "severity", "user_type",
    "quote_worthy", "feature_requested", "coder", "notes", "coder2_primary_theme",
]


def _id(*parts: str) -> str:
    return hashlib.sha1("|".join(parts).encode()).hexdigest()[:10]


def fetch_ios(country: str = "us", pages: int = 10) -> list[dict]:
    rows = []
    for page in range(1, pages + 1):
        url = (f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/"
               f"id={IOS_APP_ID}/sortby=mostrecent/json")
        try:
            with urllib.request.urlopen(url, timeout=20) as resp:
                data = json.load(resp)
        except Exception as e:
            print(f"iOS page {page}: {e}")
            break
        entries = data.get("feed", {}).get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        if not entries:
            break
        for e in entries:
            if "im:rating" not in e:  # first entry can be app metadata
                continue
            rows.append({
                "review_id": "ios-" + _id(e["id"]["label"]),
                "source": "ios",
                "date": e.get("updated", {}).get("label", "")[:10],
                "rating": int(e["im:rating"]["label"]),
                "title": e.get("title", {}).get("label", ""),
                "text": e.get("content", {}).get("label", ""),
                "app_version": e.get("im:version", {}).get("label", ""),
            })
    return rows


def fetch_android(count: int = 500) -> list[dict]:
    try:
        from google_play_scraper import Sort, reviews
    except ImportError:
        print("google-play-scraper not installed; skipping Android")
        return []
    result, _ = reviews(ANDROID_PACKAGE, lang="en", country="us", sort=Sort.NEWEST, count=count)
    return [{
        "review_id": "and-" + _id(r["reviewId"]),
        "source": "android",
        "date": r["at"].strftime("%Y-%m-%d"),
        "rating": int(r["score"]),
        "title": "",
        "text": r.get("content") or "",
        "app_version": r.get("appVersion") or "",
    } for r in result]


def sample(df: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    """Equal split across stores, and within each store proportional to the
    rating mix so the sample keeps the real balance of happy and unhappy users."""
    parts = []
    per_source = n // max(df["source"].nunique(), 1)
    for _, g in df.groupby("source"):
        k = min(per_source, len(g))
        for _, by_rating in g.groupby("rating"):
            take = min(len(by_rating), max(1, round(k * len(by_rating) / len(g))))
            parts.append(by_rating.sample(take, random_state=seed))
    out = pd.concat(parts).sample(frac=1, random_state=seed).head(n)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=150)
    ap.add_argument("--days", type=int, default=90, help="keep reviews from the last N days")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rows = fetch_ios() + fetch_android()
    df = pd.DataFrame(rows).drop_duplicates("review_id")
    df = df[df["text"].str.split().str.len() >= 5]  # drop "great app" style one-liners
    cutoff = (datetime.now(timezone.utc) - timedelta(days=args.days)).strftime("%Y-%m-%d")
    df = df[df["date"] >= cutoff]
    df.to_csv(HERE / "raw_reviews.csv", index=False)
    print(f"Pulled {len(df)} reviews since {cutoff}: {df['source'].value_counts().to_dict()}")

    sheet = sample(df, args.sample, args.seed)
    for col in CODING_COLUMNS:
        sheet[col] = ""
    sheet.to_csv(HERE / "review_coding_sheet.csv", index=False)
    print(f"Wrote {len(sheet)} reviews to review_coding_sheet.csv. "
          f"Rating mix: {sheet['rating'].value_counts().sort_index().to_dict()}")


if __name__ == "__main__":
    main()
