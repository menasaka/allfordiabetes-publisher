"""
Site-specific settings for allfordiabetes.com.

Everything that ties this publisher to one website lives in this file.
The site runs on Next.js + Sanity (Vercel), so articles are published straight to Sanity.
"""

SITE_NAME = "All for Diabetes"
SITE_DOMAIN = "allfordiabetes.com"
SITE_URL = "https://allfordiabetes.com"
PAGE_ICON = "🩺"

# OpenAI model used for articles and FAQs (override with the OPENAI_MODEL secret)
DEFAULT_OPENAI_MODEL = "gpt-4o"

# ------------------------------------------------------------------------------
# Categories: the site's Sanity category titles (they must match exactly).
# Value = Sanity document id, for reference.
# ------------------------------------------------------------------------------
CATEGORY_MAP = {
    "Diabetes Type 2": "category-diabetes-type-2",
    "Diabetes type 1": "category-diabetes-type-1",
    "Gestational Diabetes": "category-gestational-diabetes",
    "Diabetes News": "category-diabetes_news",
    "Diabetes and Coronavirus": "category-diabetes-and-coronavirus",
}
DEFAULT_CATEGORIES = ["Diabetes Type 2"]
# Every new article is also put in these categories (after the chosen ones, so the main category is unchanged).
# "Diabetes News" = the site's news section (/category/diabetes_news/ and the "Diabetes news" sidebar box).
ALWAYS_CATEGORIES = ["Diabetes News"]

# ------------------------------------------------------------------------------
# Writing rules
# ------------------------------------------------------------------------------
SYSTEM_PROMPT = (
    "You write health education articles for All for Diabetes (allfordiabetes.com), "
    "an independent information site about type 1, type 2 and gestational diabetes and prediabetes, "
    "for adults in the United States. "
    "Tone: Clear, practical, encouraging, plain-English, active voice, short simple sentences. Write like an experienced "
    "diabetes educator explaining things to a friend, not like a textbook. Never blame or shame the reader for their "
    "weight, food choices or blood sugar numbers. "
    "Do NOT use em dashes, AI-style labels, or generic intros such as 'In today's world'. "
    "Length: ~1,200 words. Structure: Question-based H2 headings. "
    "Medical accuracy rules: Only state well-established facts that match current mainstream guidance "
    "(for example the American Diabetes Association Standards of Care, the CDC, the NIDDK and major academic "
    "medical centers). Never invent statistics, studies, quotes, doctors, or patient stories. "
    "If you mention a number (for example A1C or blood sugar targets), use widely accepted figures only, keep them "
    "general, and say that personal targets are set with a doctor. "
    "Never give personal dosing instructions (insulin units, carb ratios, pill doses) and never tell readers to start, "
    "stop or change a medication or insulin on their own; say to talk with their doctor, diabetes care team or "
    "pharmacist first. Never claim a food, supplement, diet or product cures or reverses diabetes; you may say "
    "type 2 diabetes can sometimes go into remission with weight loss under medical care. "
    "All for Diabetes is not a clinic. Do not invite readers to book appointments with All for Diabetes; "
    "encourage them to talk with their own doctor, an endocrinologist, or a certified diabetes care and education "
    "specialist. "
    "CRITICAL LENGTH RULE: You MUST write 3 to 4 detailed paragraphs under EVERY SINGLE H2 to ensure "
    "the article reaches 1,200+ words. No brief summaries."
)

ARTICLE_PROMPT_TEMPLATE = """
Write an in-depth, trustworthy health education article for All for Diabetes about: "{topic}".

Strict Article Requirements:
1. Every major section must start with a question-based H2 heading ending in a question mark (e.g., '## What Is a Normal A1C Level?').
2. Include at least 5 to 7 question-based H2 sections.
3. Under EVERY SINGLE H2 heading, write 3 to 4 well-developed paragraphs covering symptoms, causes, risk factors, blood sugar monitoring, treatment options (lifestyle, eating plan, physical activity, medications, insulin), complications, or prevention as they relate to the topic.
4. One H2 section must explain when to get help, including signs that need urgent care (for example very low blood sugar with confusion, fainting or seizures; very high blood sugar with vomiting, deep fast breathing, fruity-smelling breath or extreme thirst, which can mean diabetic ketoacidosis; or chest pain or stroke signs). It must say to call 911 in an emergency.
5. Keep individual sentences short, natural, and clear. Avoid filler phrases, em dashes (—), and artificial AI introductions.
6. Do not include an FAQ section in this body content (the FAQ is generated separately).
7. Do not add a disclaimer (one is added automatically).
8. Total word count must be 1,200+ words.
"""

FAQ_SYSTEM_PROMPT = (
    "You are a careful diabetes educator who writes topic-specific FAQ sections about diabetes and prediabetes. "
    "You always reply with valid JSON."
)

FAQ_PROMPT_TEMPLATE = """
Generate 12 frequently asked questions and answers for an article titled: "{topic}".

Strict Specifications:
1. Every question MUST be directly about the topic of the title above. These are the questions a reader of that specific article would ask. Do not drift to unrelated conditions or treatments that the title does not mention, and do not ask generic site questions (who wrote this, is this medical advice, where can I learn more).
2. Write as All for Diabetes, an independent diabetes information site. All for Diabetes is not a clinic and does not treat patients.
3. Requirements for every answer: EXACTLY 3 sentences. Helpful, encouraging, plain-English tone. Short, natural sentences in active voice. No em dashes.
4. Never invent statistics, studies, prices, brand claims, or guarantees. Never give personal dosing instructions or advise starting, stopping or changing a medication or insulin. Never claim a food or supplement cures diabetes.
5. The last question must be about when to get help for this topic, and it must mention calling 911 in an emergency.

Output Format:
Return ONLY a JSON object of this shape:
{{"faqs": [{{"question": "...", "answer": "..."}}, ...]}}
with exactly 12 items.
"""

# Sample topics for the quick-select buttons
SAMPLE_TOPICS = [
    "Early Signs of Type 2 Diabetes Many People Miss",
    "What Your A1C Number Means and How to Bring It Down",
    "Prediabetes: How to Stop It From Turning Into Type 2 Diabetes",
    "Low Blood Sugar: Symptoms, Causes and What to Do Right Away",
]

# ------------------------------------------------------------------------------
# Formatting
# ------------------------------------------------------------------------------
H2_OPEN_TAG = "<h2>"
# New article URLs have at most this many words. OpenAI picks the main keyword (SLUG_PROMPT);
# if that fails, the first words of the title are used with filler words ("what", "and", "the") dropped.
# A "-2" is still added when the URL is already taken.
SLUG_MAX_WORDS = 4
SLUG_PROMPT = """
Write a short SEO URL slug for a diabetes health article titled: "{topic}".

Rules:
- At most {max_words} words in total, lowercase, joined by hyphens. Every number counts as a word
  ("type-2-diabetes" is 3 words, "glp-1" is 2 words).
- Use the article's main search keyword, the words people would type into Google. Keep the most important
  words and drop filler words (what, how, your, and, the, of, to).
- Plain English words only. No dates, no site name, no stop words at the start or end.

Examples: "What Your A1C Number Means and How to Bring It Down" -> "lower-a1c-levels";
"Early Signs of Type 2 Diabetes Many People Miss" -> "type-2-diabetes-signs".

Return ONLY JSON: {{"slug": "..."}}
"""
FAQ_HEADING = "Frequently Asked Questions"
SHORTCODES_LIST = []

KEYWORDS_TO_BOLD = [
    "type 2 diabetes",
    "type 1 diabetes",
    "gestational diabetes",
    "prediabetes",
    "blood sugar",
    "A1C",
    "insulin resistance",
    "hypoglycemia",
    "hyperglycemia",
    "diabetic ketoacidosis",
    "endocrinologist",
    "diabetes care team",
]

# Internal links (all checked: return HTTP 200 on 2026-11-14; the URLs stay the same after the move to Vercel)
INTERNAL_LINKS = [
    {
        "keywords": ["type 2 diabetes"],
        "html": '<a href="https://allfordiabetes.com/type-2-diabetes-the-basics/">the basics of type 2 diabetes</a>',
    },
    {
        "keywords": ["early signs", "symptoms of diabetes", "warning signs"],
        "html": '<a href="https://allfordiabetes.com/the-first-symptoms-of-diabetes/">the first symptoms of diabetes</a>',
    },
    {
        "keywords": ["type 1 diabetes"],
        "html": '<a href="https://allfordiabetes.com/5-reasons-that-may-explain-why-type-1-diabetes/">why type 1 diabetes is on the rise</a>',
    },
    {
        "keywords": ["gestational diabetes", "pregnancy", "pregnant"],
        "html": '<a href="https://allfordiabetes.com/gestational_diabetes/">gestational diabetes</a>',
    },
    {
        "keywords": ["prediabetes", "prevent type 2", "prevention"],
        "html": '<a href="https://allfordiabetes.com/prevention-delay-of-type-2-diabetes/">preventing or delaying type 2 diabetes</a>',
    },
    {
        "keywords": ["insulin resistance", "weight loss", "weight"],
        "html": '<a href="https://allfordiabetes.com/are-your-weight-issues-tied-to-insulin-resistance/">weight and insulin resistance</a>',
    },
    {
        "keywords": ["blood sugar", "glucose"],
        "html": '<a href="https://allfordiabetes.com/how-to-lower-your-blood-sugar-naturally/">lowering blood sugar naturally</a>',
    },
    {
        "keywords": ["healthy foods", "diet", "eating plan", "nutrition"],
        "html": '<a href="https://allfordiabetes.com/nine-healthy-foods-for-diabetes/">healthy foods for diabetes</a>',
    },
    {
        "keywords": ["foods to avoid", "added sugar", "sugary drinks"],
        "html": '<a href="https://allfordiabetes.com/foods-to-avoid-in-diabetes/">foods to avoid with diabetes</a>',
    },
    {
        "keywords": ["carbohydrates", "carbs", "carbohydrate"],
        "html": '<a href="https://allfordiabetes.com/carbohydrate/">carbohydrates and diabetes</a>',
    },
    {
        "keywords": ["exercise", "physical activity"],
        "html": '<a href="https://allfordiabetes.com/diabetes-and-exercise-compatible-but-not-always/">diabetes and exercise</a>',
    },
    {
        "keywords": ["medications", "metformin", "medication"],
        "html": '<a href="https://allfordiabetes.com/diabetes_mellitus_type_2_medications/">type 2 diabetes medications</a>',
    },
    {
        "keywords": ["neuropathy", "nerve damage", "numbness"],
        "html": '<a href="https://allfordiabetes.com/neuropathy-screening-and-treatment/">neuropathy screening and treatment</a>',
    },
    {
        "keywords": ["foot care", "feet", "foot"],
        "html": '<a href="https://allfordiabetes.com/diabetes-foot-care/">diabetes foot care</a>',
    },
    {
        "keywords": ["retinopathy", "eye exam", "vision"],
        "html": '<a href="https://allfordiabetes.com/retinopathy-screening-and-treatment/">retinopathy screening</a>',
    },
    {
        "keywords": ["sleep apnea", "sleep"],
        "html": '<a href="https://allfordiabetes.com/sleep-apnea-may-increase-insulin-resistance/">sleep apnea and insulin resistance</a>',
    },
]

FALLBACK_LINK_SENTENCE = (
    '<p>Want to learn more? Read about '
    '<a href="https://allfordiabetes.com/type-2-diabetes-the-basics/">the basics of type 2 diabetes</a> and '
    '<a href="https://allfordiabetes.com/how-to-lower-your-blood-sugar-naturally/">lowering blood sugar naturally</a>.</p>'
)

# Added at the end of every post (after the FAQ)
MEDICAL_DISCLAIMER_HTML = (
    '<p><em>This article is for general information only and is not medical advice. '
    'Always talk with your doctor or diabetes care team about your symptoms, blood sugar targets and treatment, '
    'and never change your medication or insulin without their advice. '
    'If you have signs of very low or very high blood sugar that do not improve, or you feel very unwell, '
    'call 911 or go to the nearest emergency room.</em></p>'
)

# ------------------------------------------------------------------------------
# Meta description
# ------------------------------------------------------------------------------
META_DESC_SUFFIX = "Learn more at All for Diabetes."
META_DESC_FALLBACK = "Clear, trustworthy information on living with diabetes, blood sugar control and prevention."
META_DESC_MAX_CHARS = 160

# ------------------------------------------------------------------------------
# Images
# ------------------------------------------------------------------------------
IMAGE_COUNT = 1
IMAGE_SIZE = (1200, 800)  # featured image size (photo is cropped to fill it)
TITLE_CARD_COLORS = ((14, 59, 102), (38, 166, 154))  # deep blue -> teal

# Open-license topic photos (Openverse). CC0 only: free for commercial use, no attribution required.
USE_OPEN_PHOTOS = True
OPENVERSE_API = "https://api.openverse.org/v1/images/"
OPENVERSE_SOURCES = ["stocksnap"]          # tried first
OPENVERSE_FALLBACK_SOURCES = ["stocksnap", "flickr", "wikimedia"]  # broader second pass
OPENVERSE_LICENSE = "cc0,pdm"
PHOTO_OVERLAY_ALPHA = 30    # 0-255 light tint over the whole photo (0 = none)
TITLE_BAR_RATIO = 0.20      # title strip covers the top 20% of the image
TITLE_BAR_ALPHA = 150       # 0-255 darkness of the title strip
TITLE_MAX_FONT = 44         # max title font size in px (on a 1200px-wide image)
SHOW_DOMAIN_ON_IMAGE = False
GRAYSCALE_IMAGES = False    # True = every featured image is saved in black and white (recurrentdepression uses True)

PHOTO_QUERY_PROMPT = """
Suggest stock photo search phrases for a featured image for a diabetes health article titled: "{topic}".

Rules:
- 6 phrases, best first. Each is 1 to 3 plain visual words that a free stock photo site would tag
  (for example: "salad bowl", "vegetables", "walking park", "doctor patient", "running shoes",
  "fruit market", "pregnant woman", "family dinner", "cooking kitchen", "cycling").
- Positive, healthy images. Nothing distressing: no wounds, amputations, needles in skin, blood close-ups
  or hospital emergencies; no cakes, candy or junk food piles.
- Describe things a camera can photograph. No medical jargon, no brand names, no drug names, no text.
- Mix specific phrases with broader fallbacks.

Return ONLY JSON: {{"queries": ["...", "..."]}}
"""
# Used if OpenAI can't suggest phrases
DEFAULT_PHOTO_QUERIES = ["salad bowl", "vegetables", "walking park", "doctor patient", "fruit", "cycling"]

# Words that suggest the wrong kind of image for a health site
PHOTO_TITLE_BLOCKLIST = [
    "quote", "typography", "text", "logo", "sign", "advert", "poster", "cure", "dog", "cat",
    "chart", "graph", "map", "diagram", "screenshot", "etching", "engraving", "illustration",
    "blood", "wound", "amputation", "syringe", "needle", "skull", "grave", "cemetery",
    "cake", "candy", "donut", "doughnut", "soda",
]

# ------------------------------------------------------------------------------
# Daily news auto-publisher (autopublish.py, run by GitHub Actions)
# ------------------------------------------------------------------------------
TIMEZONE = "America/Los_Angeles"
PUBLISH_HOURS = [9, 14]          # local times: 9am = 1st headline, 2pm = 2nd headline
LAST_CATCH_UP_HOUR = 17          # a missed slot is made up by the hourly runs until 5:59pm
NEWS_QUERY = 'diabetes OR prediabetes OR "blood sugar" OR insulin OR A1C OR "GLP-1"'
NEWS_WINDOW = "1d"               # Google News "when:" filter (last 24 hours)
NEWS_FALLBACK_WINDOW = "3d"      # used if nothing new in the last day
NEWS_SOURCE_BLOCKLIST = ["YouTube", "TikTok", "Facebook", "Instagram", "Reddit"]
NEWS_CATEGORY_NAMES = ["Diabetes News"]
# Fallback filter when OpenAI can't judge the headlines
NEWS_KEYWORD_RE = r"\b(diabetes|diabetic|prediabetes|insulin|blood sugar|A1C|GLP-1|metformin)\b"

NEWS_PICK_PROMPT = """
Below are recent news headlines found by searching Google News for diabetes, prediabetes, blood sugar, insulin and GLP-1 medicines.

{listing}

Keep ONLY headlines that are genuinely about human diabetes or prediabetes health: research, treatments,
medications, insulin, devices (glucose monitors, pumps), eating and exercise, symptoms, causes, risk factors,
complications, prevention, or patient care. REJECT stock market and company earnings stories, drug pricing
politics with no health content, pet diabetes, celebrity gossip, crime stories, reports about an individual's death,
weight-loss product promotions, compounded or knock-off drug sales, miracle-cure claims, and non-English headlines.

For each kept headline write an original, accurate, SEO-friendly article title for All for Diabetes
(55-75 characters, plain English, no clickbait, no em dashes, do not copy the headline word for word,
do not promise cures).

Return ONLY JSON: {{"picks": [{{"index": <number>, "title": "..."}}]}}
Return an empty list if none qualify.
"""

NEWS_ARTICLE_EXTRA = """
News context: this article is prompted by a recent news report.
- Headline: "{headline}"
- Published by: {source}

How to use it:
- In the first section, briefly say what the news report covers, using ONLY what the headline states.
  You have not read the report, so do NOT invent study details, numbers, names, dates, quotes, or results.
  Use cautious wording such as "a recent report from {source} highlights..." and "early research suggests".
- Then write a helpful, accurate explainer on the wider topic for readers living with diabetes or prediabetes:
  background, what is already well established, what it may mean for patients, and practical next steps.
- Do not include a link or a sources list (one is added automatically).
"""

# ------------------------------------------------------------------------------
# Sanity (the live site: Next.js + Sanity on Vercel)
# ------------------------------------------------------------------------------
SANITY_PROJECT_ID = "wlcff47a"
SANITY_DATASET = "production"
# Every article is credited to the site's author (Sanity document id).
SANITY_AUTHOR_ID = "author-david"
# Marker for auto-published news posts (used by the daily slot count).
SOURCE_MARKER = "afd-news-source"
