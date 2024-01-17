from src.searchers.wikipedia_searcher import search_wikipedia
from src.searchers.weather_searcher import search_weather
from src.checkers.text_space_checker import check_text_space_handle
from src.checkers.text_spell_checker import check_text_spell_handle

keyword_handle = {
    'wikipedia': search_wikipedia,
    'weather': search_weather,
    'text_space': check_text_space_handle,
    'text_spell': check_text_spell_handle,
}
