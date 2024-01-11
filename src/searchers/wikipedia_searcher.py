import wikipedia
from utils.log_util import configure_logger

logger = configure_logger(__name__, 'wikipedia_search.log')

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=1)
        logger.info(f"wikipedia_searcher Success query - {query}")
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"wikipedia_searcher DisambiguationError query - {query}")
        return "请提供更具体的查询，以便我找到相关的信息。"
    except wikipedia.exceptions.PageError as e:
        logger.warning(f"wikipedia_searcher PageError query - {query}")
        return "找不到与查询相关的内容。"
