from src.checkers.text_spell_checker import check_text_spell, check_text_spell_handle
import pytest
import os
import shutil

TEST_FOLDER = 'tests/checkers/handled'

@pytest.fixture
def cleanup_fixture():
    yield
    if os.path.exists(TEST_FOLDER):
        shutil.rmtree(TEST_FOLDER)

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

def test_spell_checker_with_file_path(cleanup_fixture):
    input_file_path = "tests/checkers/resources/test_text_spell_checker_input.txt"
    output_file_path = "tests/checkers/handled/test_text_spell_checker_output.txt"
    expected_output_file_path = "tests/checkers/resources/test_text_spell_checker_excepted_output.txt"
    actual_output_file_path = check_text_spell_handle(file_path=input_file_path, output_path=output_file_path)
    assert actual_output_file_path == output_file_path
    with open(actual_output_file_path, 'r', encoding='utf-8') as f:
        auctal_output_text = f.read()
    with open(expected_output_file_path, 'r', encoding='utf-8') as f:
        expected_output_text = f.read()
    assert auctal_output_text == expected_output_text