
def mock_weather_searcher_get_direct(mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = [{'lat': 40.7128, 'lon': -74.0060}]

def mock_weather_searcher_get_weather(mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            'main': {'temp': 25.5},
            'weather': [{'description': 'Clear sky'}]
        }