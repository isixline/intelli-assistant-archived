import pytest
from unittest.mock import patch
from src.searchers.weather_searcher import get_coordinates, get_weather_by_coordinates, search_weather

@pytest.fixture
def mock_openweathermap_response():
    return {
        'lat': 40.7128,
        'lon': -74.0060,
        'main': {'temp': 25.5},
        'weather': [{'description': 'Clear sky'}]
    }

@patch('src.searchers.weather_searcher.requests.get')
def test_get_coordinates(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [{'lat': 40.7128, 'lon': -74.0060}]

    api_key = 'your_api_key'
    city = 'New York'
    latitude, longitude = get_coordinates(api_key, city)

    assert latitude == 40.7128
    assert longitude == -74.0060

@patch('src.searchers.weather_searcher.requests.get')
def test_get_weather_by_coordinates(mock_requests_get, mock_openweathermap_response):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_openweathermap_response

    api_key = 'your_api_key'
    latitude, longitude = 40.7128, -74.0060
    result = get_weather_by_coordinates(api_key, latitude, longitude)

    assert "Current weather: Temperature 25.5 °C, Clear sky" in result

@patch('os.getenv')
@patch('src.searchers.weather_searcher.get_coordinates')
@patch('src.searchers.weather_searcher.get_weather_by_coordinates')
def test_search_weather(mock_get_weather, mock_get_coordinates, mock_os_getenv):
    mock_os_getenv.return_value = 'your_api_key'
    mock_get_coordinates.return_value = (40.7128, -74.0060)
    mock_get_weather.return_value = "Current weather: Temperature 25.5 °C, Clear sky"

    city = 'New York'
    result = search_weather(city=city)

    assert "Current weather: Temperature 25.5 °C, Clear sky" in result
