import wikipedia

def mock_wikipedia_summary(mock, query):
        mock.return_value = query

def mock_wikipedia_disambiguation_error(mock, query):
        mock.side_effect = wikipedia.exceptions.DisambiguationError(['Option1', 'Option2'], query)

def mock_wikipedia_page_error(mock, query):
        mock.side_effect = wikipedia.exceptions.PageError(query)

