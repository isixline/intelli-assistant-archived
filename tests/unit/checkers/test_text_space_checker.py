from src.checkers.text_space_checker import check_text_space, check_text_space_handle
import pytest
import shutil
import os

TEST_FOLDER = 'tests/test_data/handled'

@pytest.fixture
def cleanup_fixture():
    yield
    if os.path.exists(TEST_FOLDER):
        shutil.rmtree(TEST_FOLDER)

def test_check_text_space_with_english_only():
    input_text = "Hello"
    expected_output = "Hello"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_with_chinese_only():
    input_text = "世界"
    expected_output = "世界"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_with_english_and_chinese():
    input_text = "Hello世界"
    expected_output = "Hello 世界"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_with_english_and_chinese_and_english():
    input_text = "Hello世界Python"
    expected_output = "Hello 世界 Python"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_with_english_and_chinese_and_english_and_chinese():
    input_text = "Hello世界Python编程"
    expected_output = "Hello 世界 Python 编程"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_with_english_and_chinese_and_with_more_spaces():
    input_text = "Hello  世界  Python  编程"
    expected_output = "Hello 世界 Python 编程"
    assert check_text_space(text=input_text) == expected_output

def test_check_text_space_handle_with_file_path(cleanup_fixture):
    input_file_path = "tests/test_data/test_text_space_checker_input.txt"
    output_file_path = "tests/test_data/handled/test_text_space_checker_output.txt"
    expected_output_file_path = "tests/test_data/test_text_space_checker_excepted_output.txt"
    actual_output_file_path = check_text_space_handle(file_path=input_file_path, output_path=output_file_path)
    assert actual_output_file_path == output_file_path
    with open(actual_output_file_path, 'r', encoding='utf-8') as f:
        auctal_output_text = f.read()
    with open(expected_output_file_path, 'r', encoding='utf-8') as f:
        expected_output_text = f.read()
    assert auctal_output_text == expected_output_text



