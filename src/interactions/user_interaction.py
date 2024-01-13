from src.utils.log_util import configure_logger
from src.distributors.keyword_distributor import keyword_handle

logger = configure_logger(__name__, 'user_interaction.log')

def generate_prompt():
    keywords = ', '.join(keyword_handle.keys())
    return f"Enter a keyword ({keywords}) to search, or 'exit' to end the program:"

def perform_search(keyword, search_query):
    print(f"Searching for {keyword}...")
    print(search_query)
    search_function = keyword_handle.get(keyword)
    print(search_function)
    if search_function:
        result = search_function(search_query)
        logger.info(f"user_input: {keyword} {search_query}")
        logger.info(f"search_result: {result}")
        return result
    else:
        return "I'm sorry, I don't understand what you're asking for."

def interaction_handle():
    print("Hello! I'm your personal intelligent assistant.")

    while True:
        user_input = input(generate_prompt())
        
        if user_input.lower() == "exit":
            logger.info("user exit")
            print("Goodbye and have a nice day!")
            break

        keyword, *search_query = user_input.lower().split(maxsplit=1)

        while not search_query:
            search_query = input("Please provide additional input after the keyword.")

        search_result = perform_search(keyword, search_query)
        print(search_result)
