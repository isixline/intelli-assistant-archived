import wikipedia
from unittest.mock import patch
from src.searchers.wikipedia_searcher import search_wikipedia
from tests.mocks.wikipedia_searcher_mock import mock_wikipedia_summary, mock_wikipedia_disambiguation_error, mock_wikipedia_page_error

@patch('src.searchers.wikipedia_searcher.wikipedia.summary')
def test_search_wikipedia_summary_success(mock_summary):
    search = 'Python programming language'
    mock_wikipedia_summary(mock_summary, search)

    result = search_wikipedia(search=search)

    assert result == "Python programming language"
    mock_summary.assert_called_once_with(search, sentences=1)

@patch('src.searchers.wikipedia_searcher.wikipedia.summary')
def test_search_wikipedia_disambiguation_error(mock_summary):
    search = 'Ambiguous search'
    mock_wikipedia_disambiguation_error(mock_summary)

    result = search_wikipedia(search=search)

    assert result == 'Please provide a more specific search.'
    mock_summary.assert_called_once_with(search, sentences=1)

@patch('src.searchers.wikipedia_searcher.wikipedia.summary')
def test_search_wikipedia_page_error(mock_summary):
    search = 'Nonexistent Page'
    mock_wikipedia_page_error(mock_summary)
    
    result = search_wikipedia(search=search)

    assert result == 'Sorry, no results found.'
    mock_summary.assert_called_once_with(search, sentences=1)

