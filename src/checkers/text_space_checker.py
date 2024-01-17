import re
from src.utils.file_util import handle_file

def check_text_space(text):
    pattern = re.compile(r'(?<=[a-zA-Z])\s*(?=[\u4e00-\u9fa5])|(?<=[\u4e00-\u9fa5])\s*(?=[a-zA-Z])')
    formatted_text = re.sub(pattern, ' ', text)

    return formatted_text

def check_text_space_handle(**kwargs):
    if 'text' in kwargs:
        text = kwargs.get('text')
        formatted_text = check_text_space(text)
        return formatted_text
    elif 'file_path' in kwargs:
        file_path = kwargs.get('file_path')
        output_path = kwargs.get('output_path')
        output_path = handle_file(file_path, output_path, check_text_space)  
        return output_path
    else:
        raise Exception('Invalid input!')
             
