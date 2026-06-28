import feedparser

from services.myrss import RSS_FEEDS
from models import Article



def get_articles(limit=3) -> list[Article]:
    articles: list[Article] = []

    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo:
                continue

            for entry in feed.entries[:limit]:
                articles.append(
                    Article(
                        source=feed.feed.get("title", "Unknown Source"),
                        title=entry.get("title", ""),
                        link=entry.get("link", ""),
                        summary=entry.get("summary", ""),
                        published=entry.get("published", "No date"),
                    )
                )

                # if len(articles) >= limit:
                #     return articles

        except Exception as e:
            print(f"Error processing feed {feed_url}: {e}")

    return articles
