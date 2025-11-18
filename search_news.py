from gnews import GNews
from typing import Optional, Dict, Any, List
from model import CompanyNewsResult, NewsArticle

def search_news_by_company(company_name: str, num_articles: int = 10) -> Optional[CompanyNewsResult]:
    """
    Searches Google News for articles related to a specific company name using GNews.
    """
    if not company_name:
        print("Error: Company name cannot be empty.")
        return None

    try:
        # Initialize GNews client (using English settings for broad results)
        google_news = GNews(
            language='en', 
            country='US', 
            period='7d', 
            max_results=num_articles
        )
        
        query = f'"{company_name}" stock' 
        raw_results = google_news.get_news(query)

        if not raw_results:
            return CompanyNewsResult(company_name=company_name, articles_found=0, articles=[])

        processed_articles: List[NewsArticle] = []
        for item in raw_results:
            article = NewsArticle(
                title=item.get('title', 'No Title'),
                description=item.get('description', 'No Description'),
                published_date=item.get('published date', 'N/A'),
                url=item.get('url', '#'),
                source=item.get('publisher', {}).get('title', 'Unknown Source')
            )
            processed_articles.append(article)

        return CompanyNewsResult(
            company_name=company_name,
            articles_found=len(processed_articles),
            articles=processed_articles
        )

    except Exception as e:
        print(f"Error during GNews search for '{company_name}': {e}")
        return None