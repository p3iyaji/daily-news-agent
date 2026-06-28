from news_agent import get_articles

articles = get_articles()

print(f"Found {len(articles)} articles\n")

for article in articles[:50]:
    print("=" * 50)
    print(article.title)
    print(article.link)
    print(article.published)

