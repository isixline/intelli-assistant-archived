import wikipedia

def mock_wikipedia_summary(mock, search):
        mock.return_value = search

def mock_wikipedia_disambiguation_error(mock):
        mock.side_effect = wikipedia.exceptions.DisambiguationError(['Option1', 'Option2'], 'Please provide a more specific search.')

def mock_wikipedia_page_error(mock):
        mock.side_effect = wikipedia.exceptions.PageError('Sorry, no results found.')

