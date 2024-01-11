from searchers.wikipedia_searcher import search_wikipedia
from searchers.weather_searcher import search_weather

keyword_handle = {
    'wikipedia': search_wikipedia,
    'weather': search_weather,
}
