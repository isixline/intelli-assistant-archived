import pytest
from unittest.mock import patch
from src.searchers.weather_searcher import get_coordinates, get_weather_by_coordinates, search_weather
from tests.mocks.weather_searcher_mock import mock_weather_searcher_get_direct, mock_weather_searcher_get_weather

@patch('src.searchers.weather_searcher.requests.get')
def test_get_coordinates(mock_requests_get):
    mock_weather_searcher_get_direct(mock_requests_get)
    api_key = 'your_api_key'
    city = 'New York'
    latitude, longitude = get_coordinates(api_key, city)

    assert latitude == 40.7128
    assert longitude == -74.0060

@patch('src.searchers.weather_searcher.requests.get')
def test_get_weather_by_coordinates(mock_requests_get):
    mock_weather_searcher_get_weather(mock_requests_get)

    api_key = 'your_api_key'
    latitude, longitude = 40.7128, -74.0060
    result = get_weather_by_coordinates(api_key, latitude, longitude)

    assert "Current weather: Temperature 25.5 °C, Clear sky" in result