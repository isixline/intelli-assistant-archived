from src.interactions.user_interaction import split_keyword_and_args, split_args, user_input_handle

def test_split_user_input_with_keyword():
    input_text = "wikipedia"
    expected_keyword = "wikipedia"
    excepted_args = ""
    assert split_keyword_and_args(input_text) == (expected_keyword, excepted_args)

def test_split_user_input_with_keyword_and_one_arg():
    input_text = "wikipedia search=Python"
    expected_keyword = "wikipedia"
    excepted_args = "search=Python"
    assert split_keyword_and_args(input_text) == (expected_keyword, excepted_args)

def test_split_user_input_with_keyword_and_two_args():
    input_text = "wikipedia search=Python page=1"
    expected_keyword = "wikipedia"
    excepted_args = "search=Python page=1"
    assert split_keyword_and_args(input_text) == (expected_keyword, excepted_args)

def test_split_args_with_one_arg():
    args_string = "search=Python"
    expected_args = {"search": "Python"}
    assert split_args(args_string) == expected_args

def test_split_args_with_two_args():
    args_string = "search=Python page=1"
    expected_args = {"search": "Python", "page": "1"}
    assert split_args(args_string) == expected_args

def test_split_args_with_two_args_and_include_quotes():
    args_string = "search=\"Python\" page=1"
    expected_args = {"search": "Python", "page": "1"}
    assert split_args(args_string) == expected_args

def test_split_args_with_two_args_and_include_quotes_and_spaces():
    args_string = "search=\"Python programming\" page=1"
    expected_args = {"search": "Python programming", "page": "1"}
    assert split_args(args_string) == expected_args

def test_handle_user_input_with_keyword():
    input_text = "wikipedia"
    expected_keyword = "wikipedia"
    excepted_args = {}
    assert user_input_handle(input_text) == (expected_keyword, excepted_args)

def test_handle_user_input_with_keyword_and_one_arg():
    input_text = "wikipedia search=Python"
    expected_keyword = "wikipedia"
    excepted_args = {"search": "Python"}
    assert user_input_handle(input_text) == (expected_keyword, excepted_args)

def test_handle_user_input_with_keyword_and_two_args():
    input_text = "wikipedia search=Python page=1"
    expected_keyword = "wikipedia"
    excepted_args = {"search": "Python", "page": "1"}
    assert user_input_handle(input_text) == (expected_keyword, excepted_args)
