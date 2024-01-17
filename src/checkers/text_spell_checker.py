import re
from spellchecker import SpellChecker
from src.utils.file_util import handle_file

def check_text_spell(text):
    spell = SpellChecker()
    words = re.findall(r'\b\w+\b', text)
    misspelled_words = spell.unknown(words)
    return list(misspelled_words)

def check_text_spell_handle(**kwargs):
    if 'text' in kwargs:
        text = kwargs.get('text')
        misspelled_words = check_text_spell(text)
        return misspelled_words
    elif 'file_path' in kwargs:
        file_path = kwargs.get('file_path')
        output_path = kwargs.get('output_path')
        output_path = handle_file(file_path, output_path, check_text_spell)  
        return output_path
    else:
        raise Exception('Invalid input!')