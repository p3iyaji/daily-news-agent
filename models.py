from dataclasses import dataclass

@dataclass
class Article:
    source: str
    title: str
    link: str
    summary: str
    published: str


