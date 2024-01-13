import re

def check_text_space(input_text):
    pattern = re.compile(r'(?<=[a-zA-Z])\s*(?=[\u4e00-\u9fa5])|(?<=[\u4e00-\u9fa5])\s*(?=[a-zA-Z])')
    formatted_text = re.sub(pattern, ' ', input_text)

    return formatted_text
