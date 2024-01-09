import wikipedia

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=1)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "请提供更具体的查询，以便我找到相关的信息。"
    except wikipedia.exceptions.PageError as e:
        return "找不到与查询相关的内容。"
