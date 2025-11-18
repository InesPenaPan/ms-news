from pydantic import BaseModel, Field
from typing import List

class NewsArticle(BaseModel):
    """
    Represents a single news article retrieved from a search query.
    """
    title: str = Field(..., description="The title of the news article.")
    description: str = Field(..., description="A short summary or description of the article.")
    published_date: str = Field(..., description="The date the article was published (YYYY-MM-DD format).")
    url: str = Field(..., description="The direct URL link to the original article.")
    source: str = Field(..., description="The publisher or source of the article.")

class CompanyNewsResult(BaseModel):
    """
    Structure for the overall result of a company-specific news search.
    """
    company_name: str = Field(..., description="The name of the company that was queried.")
    articles_found: int = Field(..., description="The total number of articles found.")
    articles: List[NewsArticle] = Field(..., description="A list of the structured news articles.")