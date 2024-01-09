import wikipedia

def assistant():
    print("你好！我是你的个人智能助手。有什么我可以帮助你的吗？")

    while True:
        query = input("你的问题或命令： ").lower()

        if "退出" in query:
            print("再见，祝你有美好的一天！")
            break
        elif "维基百科" in query:
            search_query = input("请问你想搜索什么？ ")
            try:
                result = wikipedia.summary(search_query, sentences=1)
                print(result)
            except wikipedia.exceptions.DisambiguationError as e:
                print("请提供更具体的查询，以便我找到相关的信息。")
        else:
            print("抱歉，我不理解你说的话。")

if __name__ == "__main__":
    assistant()
