from src.checkers.text_space_checker import check_text_space

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


