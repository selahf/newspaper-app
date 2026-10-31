import requests
from django.core.cache import cache

OPEN_LIBRARY_SEARH_URL = "https://openlibrary.org/search.json"

def search_books(query: str, limit = 3):
    """
    Searches Open Library for books matching a query.
    
    Returns a list of book results, or an empty list if the search
    fails or finds nothing.
    """
    if not query:
        return []
    
    # reuse cached results so api is not repeatedly called
    cache_key = f"open_library_search:{query.strip().lower()}:{limit}"
    cached_results = cache.get(cache_key)
    
    if cached_results is not None:
        return cached_results
    
    # tell open library what information is wanted
    params = {
        "q": query,
        "fields": (
            "key,title,author_name"
            "first_publish_year,cover_i"
        ),
        "limit": limit
    }
    
    try:
        response = requests.get( # send search request to open library
            OPEN_LIBRARY_SEARH_URL,
            params = params,
            headers = {
                "User-Agent": "NewspaperApp/1.0"
            },
            timeout = 5
        )
        response.raise_for_status()
        data = response.json()
        books = data.get("docs", [])
        cache.set(cache_key, books, 60 * 60)
        return books
    except (requests.RequestException, ValueError):
        return []