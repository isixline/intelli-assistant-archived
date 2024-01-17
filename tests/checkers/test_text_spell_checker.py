from src.checkers.text_spell_checker import check_text_spell

def test_spell_checker_with_spelling_errors():
    input_text = "Thisss is a sample sentence with speling mistakes."
    misspelled_words = check_text_spell(text=input_text)
    expected_misspelled_words = ["thisss", "speling"]
    assert set(misspelled_words) == set(expected_misspelled_words)

def test_spell_checker_without_spelling_errors():
    input_text = "This is a sample sentence without spelling mistakes."
    misspelled_words = check_text_spell(text=input_text)
    assert not misspelled_words

def test_spell_checker_empty_text():
    input_text = ""
    misspelled_words = check_text_spell(text=input_text)
    assert not misspelled_words