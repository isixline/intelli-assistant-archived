from wikipedia_searcher import search_wikipedia

def main():
    print("你好！我是你的个人智能助手。")

    while True:
        user_input = input("输入'维基百科'进行搜索，输入'退出'结束程序: ")
        
        if user_input.lower() == "退出":
            print("再见，祝你有美好的一天！")
            break

        if "维基百科" in user_input:
            search_query = input("请问你想搜索什么？ ")
            search_result = search_wikipedia(search_query)
        else:
            search_result = "抱歉，我不理解你说的话."

        print(search_result)

if __name__ == "__main__":
    main()
