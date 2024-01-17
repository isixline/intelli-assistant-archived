import wikipedia
from src.utils.log_util import configure_logger

logger = configure_logger(__name__, 'wikipedia_search.log')

def search_wikipedia(**kwargs):
    query = kwargs.get('query')
    try:
        result = wikipedia.summary(query, sentences=1)
        logger.info(f"wikipedia_searcher Success query - {query}")
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"wikipedia_searcher DisambiguationError query - {query}")
        return "Please provide a more specific query."
    except wikipedia.exceptions.PageError as e:
        logger.warning(f"wikipedia_searcher PageError query - {query}")
        return "Sorry, no results found."
