from news_agent import get_articles
from summarizer import summarize_articles
from email_builder import build_email
from email_sender import send_email
from utils import log


articles = get_articles()

seen = set()
unique_articles = []

for article in articles:
    if article.link not in seen:
        unique_articles.append(article)
        seen.add(article.link)

log("RSS", f"Fetching {unique_articles}")
log("PARSE", f"Got {len(unique_articles)} entries")


summaries = summarize_articles(unique_articles)
log("AI", f"Summarizing: {summaries}")

log("AI DONE", f"Done summarizing {len(summaries)} articles.")

html = build_email(summaries["articles"])
log("EMAIL", "Sending digest...")

send_email(html)
