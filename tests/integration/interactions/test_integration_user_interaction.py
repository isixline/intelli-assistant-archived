import unittest
from src.interactions.user_interaction import interaction_handle
from tests.mocks.wikipedia_searcher_mock import mock_wikipedia_summary
from unittest.mock import patch

@patch('src.searchers.wikipedia_searcher.wikipedia.summary')
@patch('builtins.input', side_effect=['wikipedia search=Python', 'exit'])
@patch('builtins.print')
def test_interaction_handle_with_wikipedia_keyword( mock_print, mock_input, mock_summary):
    mock_wikipedia_summary(mock_summary, "Python")
    interaction_handle()
    mock_print.assert_has_calls([
            unittest.mock.call("Hello! I'm your personal intelligent assistant."),
            unittest.mock.call("Python"),
            unittest.mock.call("Goodbye!"),
        ])



