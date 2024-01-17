import re
from spellchecker import SpellChecker

def check_text_spell(**kwargs):
    input_text = kwargs.get('text')
    spell = SpellChecker()
    words = re.findall(r'\b\w+\b', input_text)
    misspelled_words = spell.unknown(words)
    return list(misspelled_words)