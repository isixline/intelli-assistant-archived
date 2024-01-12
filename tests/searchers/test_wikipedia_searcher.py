import wikipedia
from unittest.mock import patch
from src.searchers.wikipedia_searcher import search_wikipedia

@patch('src.searchers.wikipedia_searcher.wikipedia.summary')
def test_search_wikipedia_summary_success(mock_summary):
    query = 'Python programming language'
    mock_summary.return_value = 'Python is a high-level programming language.'

    result = search_wikipedia(query)

    assert result == 'Python is a high-level programming language.'
    mock_summary.assert_called_once_with(query, sentences=1)

@patch('src.searchers.wikipedia_searcher.wikipedia.summary', side_effect=wikipedia.exceptions.DisambiguationError(['Option1', 'Option2'], 'test query'))
def test_search_wikipedia_disambiguation_error(mock_summary):
    query = 'Ambiguous Query'
    
    result = search_wikipedia(query)

    assert result == 'Please provide a more specific query.'
    mock_summary.assert_called_once_with(query, sentences=1)

@patch('src.searchers.wikipedia_searcher.wikipedia.summary', side_effect=wikipedia.exceptions.PageError('test'))
def test_search_wikipedia_page_error(mock_summary):
    query = 'Nonexistent Page'
    
    result = search_wikipedia(query)

    assert result == 'Sorry, no results found.'
    mock_summary.assert_called_once_with(query, sentences=1)
