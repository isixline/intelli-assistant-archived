import requests
from src.utils.log_util import configure_logger
import os

logger = configure_logger(__name__, 'weather_searcher.log')

def get_coordinates(api_key, city):
    geocoder_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'limit': 1,
        'appid': api_key,
    }

    try:
        response = requests.get(geocoder_url, params=params)
        data = response.json()

        if response.status_code == 200 and data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            logger.info(f"Success get {city} coordinates: {latitude}, {longitude}")
            return latitude, longitude
        else:
            logger.warning(f"Failed get coordinates: {data['message']}")
            return None, None
    except Exception as e:
        logger.error(f"Exception while getting coordinates: {str(e)}")
        return None, None

def get_weather_by_coordinates(api_key, latitude, longitude):
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'units': 'metric',
        'appid': api_key,
    }

    try:
        response = requests.get(weather_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            logger.info(f"Weather query success: - {latitude}, {longitude}")
            return f"Current weather: Temperature {temperature} °C, {description}"
        else:
            logger.warning(f"Weather query failed: {data['message']}")
            return "Sorry, unable to fetch weather information."
    except Exception as e:
        logger.error(f"Weather query exception: {str(e)}")
        return "Sorry, unable to fetch weather information."

def search_weather(city):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    latitude, longitude = get_coordinates(api_key, city)

    if latitude is not None and longitude is not None:
        return get_weather_by_coordinates(api_key, latitude, longitude)
    else:
        return "Sorry, unable to fetch weather information."
    