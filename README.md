# 🩺 All for Diabetes – SEO Article Publisher & Daily News Autopilot

Writes 1,200+ word diabetes articles with OpenAI and publishes them straight to
**https://allfordiabetes.com** (Next.js + Sanity on Vercel, Sanity project `wlcff47a`), with a
featured image, a page-specific FAQ (the site adds the FAQPage schema), internal links, SEO title and
meta description, and a medical disclaimer.

Copied from `recurrentdepression-publisher` (unchanged). Differences:

| | Recurrent Depression | All for Diabetes (this copy) |
|---|---|---|
| Sanity project | `7o8n3v2c` | `wlcff47a`, author `author-david` |
| Topic rules | depression; suicide safe-messaging; 988 | type 1 / type 2 / gestational diabetes and prediabetes; ADA/CDC/NIDDK guidance; no insulin or pill dosing; never "cures/reverses diabetes"; 911 + low/high blood sugar and DKA warning signs in every "when to get help" section |
| News search | depression / mood disorder words | `diabetes OR prediabetes OR "blood sugar" OR insulin OR A1C OR "GLP-1"`; OpenAI drops stock/earnings, pricing politics, pet diabetes, weight-loss promos, compounded-drug sales |
| News category | Psychiatry and Mental Health News + Depressive Disorders | Diabetes News |
| Photos | calm CC0 photos, black and white | healthy-living CC0 photos in colour (`GRAYSCALE_IMAGES = False`); wounds, needles, blood, sweets blocked; blue-to-teal title card |

**All site-specific settings are in `site_config.py`.**

## What an article looks like in Sanity

- `title`, `path` = `/<slug>/`: at most 4 words: OpenAI picks the main keyword, else the first meaningful title words (`SLUG_MAX_WORDS`, `SLUG_PROMPT` in site_config.py); `-2` added if taken, `publishedAt` = now, author `author-david`
- `categories`: the chosen Sanity categories (first = main category)
- `body`: the article as Portable Text, then the news source line (news posts) and the disclaimer
- `faq`: 12 questions about this article only, `mainImage`: the featured photo, `excerpt` + `seo`: meta description
- `newsSource` (news posts): headline, publisher and URL of the story it is based on (read-only field in the allfordiabetes Studio schema). It is also how the
  autopilot counts today's news posts and avoids covering the same headline twice.

New articles appear on the site at once (pages render on demand). The home page, category pages and
sitemap refresh through the Sanity webhook (`/api/revalidate`), so make sure that webhook exists
(see the site's README, launch checklist step 4).

## Daily news autopilot (GitHub Actions)

`autopublish.py` + `.github/workflows/autopublish.yml` publish two articles a day:

| Time (California) | What happens |
|---|---|
| **9:00 am** | Newest diabetes headline from Google News (last 24h, else 3 days) → article published |
| **2:00 pm** | Next newest headline not yet covered → article published |

The workflow runs hourly (`23 0,1,16-23 * * *` UTC). Each run publishes whichever slot is due but not
done yet, so a late or skipped GitHub run is made up by the next one until 5:59pm. A slot never posts
twice, even if re-run.

**Setup (once):** GitHub repo → Settings → Secrets and variables → Actions → New repository secret:
`OPENAI_API_KEY` and `SANITY_API_TOKEN` (or one secret named `AUTOMATION` with lines like
`OPENAI_API_KEY = "..."`).

**Test / run now:** repo → Actions → "Daily news auto-publish" → Run workflow →
tick `dry_run` to see which headline it would pick, or set `slot` = 1 to publish one now.

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env      # then fill in the values
streamlit run app.py
python autopublish.py --dry-run
python main.py "What Your A1C Number Means and How to Bring It Down"
```

## Streamlit Community Cloud

1. Push this folder to a new GitHub repo (`allfordiabetes-publisher`).
2. https://share.streamlit.io → **Create app** → that repo, branch `main`, file `app.py`.
3. **Advanced settings → Secrets**: paste `.streamlit/secrets.toml.example` with real values.

## Images

One 1200×800 featured image per article: OpenAI suggests healthy-living visual search phrases, the app searches
Openverse for CC0 / public-domain photos (StockSnap first), crops it and writes the title in a dark strip
across the top. If no photo is found, a branded blue-to-teal gradient card is used.
