from fastapi import FastAPI, HTTPException, status
from model import CompanyNewsResult 
from search_news import search_news_by_company 

# FastAPI initialization
app = FastAPI(
    title="MS-CompanyNews Microservice",
    description="Servicio dedicado a la búsqueda de noticias recientes por nombre de empresa (usando GNews)."
)

# ----------------------------------------------------------------------
# Get company news
# ----------------------------------------------------------------------
@app.get(
    "/news/{company_name}",
    response_model=CompanyNewsResult,
    summary="Gets recent news articles related to a specific company using GNews."
)
def get_company_news(company_name: str):
    """
    Searches for and retrieves recent news articles focusing on the specified company.
    """
    try:
        news_result = search_news_by_company(company_name)
        
        if news_result is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not retrieve news data for '{company_name}'. Search service failed."
            )
        
        return news_result
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error during news retrieval for {company_name}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error processing the news request."
        )