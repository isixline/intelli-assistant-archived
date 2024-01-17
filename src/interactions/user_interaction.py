from src.utils.log_util import configure_logger
from src.distributors.keyword_distributor import keyword_handle

logger = configure_logger(__name__, 'user_interaction.log')

def generate_prompt():
    keywords = ', '.join(keyword_handle.keys())
    return f"Enter a keyword ({keywords}) to search, or 'exit' to end the program:"

def perform_search(keyword, args):
    search_function = keyword_handle.get(keyword)
    if search_function:
        result = search_function(args)
        logger.info(f"user_input: {keyword} {args}")
        logger.info(f"search_result: {result}")
        return result
    else:
        return "I'm sorry, I don't understand what you're asking for."
    
def split_keyword_and_args(user_input):
    if ' ' not in user_input:
        keyword = user_input
        args = ""
    else:
        keyword, args = user_input.split(maxsplit=1)  
    return keyword, args
    
   
def split_args(args_string):
    result = {}
    stack = []
    key = None
    value = None
    in_quotes = False

    for char in args_string:
        if char == '=' and not in_quotes:
            key = ''.join(stack).strip()
            stack = []
        elif char == '"' and (not stack or stack[-1] != '\\'):
            if in_quotes:
                value = ''.join(stack)[1:]
                result[key] = value
                key = None
                value = None
                stack = []
                in_quotes = False
            else:
                stack.append(char)
                in_quotes = True
        elif char == ' ' and not in_quotes:
            if key is not None:
                value = ''.join(stack).strip()
                result[key] = value
                key = None
                value = None
                stack = []
        else:
            stack.append(char)

    if key is not None:
        value = ''.join(stack).strip()
        result[key] = value

    return result
    
def user_input_handle(user_input):
    keyword, args_string = split_keyword_and_args(user_input)
    args = split_args(args_string)
    return keyword, args

def interaction_handle():
    print("Hello! I'm your personal intelligent assistant.")

    while True:
        keyword, args = user_input_handle(input(generate_prompt()))
        search_result = perform_search(keyword, args)
        print(search_result)
