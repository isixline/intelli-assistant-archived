import wikipedia
from src.utils.log_util import configure_logger

logger = configure_logger(__name__, 'wikipedia_search.log')

def search_wikipedia(**kwargs):
    search = kwargs.get('search')
    try:
        result = wikipedia.summary(search, sentences=1)
        logger.info(f"wikipedia_searcher Success search - {search}")
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"wikipedia_searcher DisambiguationError search - {search}")
        return "Please provide a more specific search."
    except wikipedia.exceptions.PageError as e:
        logger.warning(f"wikipedia_searcher PageError search - {search}")
        return "Sorry, no results found."
