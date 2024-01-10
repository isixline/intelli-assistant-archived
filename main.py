from wikipedia_searcher import search_wikipedia
from log_util import configure_logger

logger = configure_logger(__name__, 'assistant.log')

def main():
    print("Hello! I'm your personal intelligent assistant.")

    while True:
        user_input = input("Enter 'wikipedia' to search and 'exit' to end the program:")
        
        if user_input.lower() == "exit":
            logger.info("user exit")
            print("Goodbye and have a nice day!")
            break

        if "wikipedia" in user_input:
            search_query = user_input.replace("wikipedia", "").strip()
            if search_query == "":
                search_query = input("What do you want to search for?")
            search_result = search_wikipedia(search_query)
        else:
            search_result = "I'm sorry, I don't understand what you're saying."

        logger.info(f"user_input: {user_input}")
        logger.info(f"search_result: {search_result}")

        print(search_result)

if __name__ == "__main__":
    main()
