from wikipedia_searcher import search_wikipedia
from log_util import configure_logger

logger = configure_logger(__name__, 'assistant.log')

def main():
    print("你好！我是你的个人智能助手。")

    while True:
        user_input = input("输入'维基百科'进行搜索，输入'退出'结束程序: ")
        
        if user_input.lower() == "退出":
            logger.info("user exit")
            print("再见，祝你有美好的一天！")
            break

        if "维基百科" in user_input:
            search_query = input("请问你想搜索什么？ ")
            search_result = search_wikipedia(search_query)
        else:
            search_result = "抱歉，我不理解你说的话."

        logger.info(f"user_input: {user_input}")
        logger.info(f"search_result: {search_result}")

        print(search_result)

if __name__ == "__main__":
    main()
