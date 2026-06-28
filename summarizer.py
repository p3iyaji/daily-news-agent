import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SUMMARY_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)


def summarize_articles(articles):
    article_text = ""

    for i, article in enumerate(articles, start=1):
        article_text += f"""
Article {i}

Title: {article.title}
Source: {article.source}
Published: {article.published}
Summary: {article.summary}
Link: {article.link}

-------------------
"""

    response = client.chat.completions.create(
        model="glm-4.7-flash",
        messages=[
            {
                "role": "user",
                "content": f"""
{SUMMARY_PROMPT}

Analyze ALL articles and return ONLY valid JSON in this format:

{{
  "articles": [
    {{
      "title": "",
      "summary": "",
      "importance": 1,
      "why_it_matters": "",
      "key_takeaways": [],
      "link": ""
    }}
  ]
}}

ARTICLES:
{article_text}
"""
            }
        ]
    )

    return json.loads(response.choices[0].message.content)
