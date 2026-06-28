import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import SUMMARY_PROMPT

load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.getenv("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/")


def summarize_articles(articles):

    article_text = ""

    for i, article in enumerate(articles, start=1):
        article_text += f"""
                Article {i}

                Title:
                {article.title}

                Source:
                {article.source}

                Published:
                {article.published}

                Summary:
                {article.summary}

                Link:
                {article.link}

                --------------------------------
            """

    response = client.responses.create(
        # model="gpt-5.4-mini",
        model="GLM-4.7-Flash",
        input=f"""
            {SUMMARY_PROMPT}

            Summarize ALL of these articles.

            {article_text}
        """
    )

    return json.loads(response.output_text)
