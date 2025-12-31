from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests


class WeatherToolInput(BaseModel):
    """Input schema for WeatherTool."""
    location: str = Field(..., description="City name or location to get weather for")


class WeatherTool(BaseTool):
    name: str = "Weather Tool"
    description: str = (
        "Get current weather information for a specific location. "
        "Provide a city name or location to retrieve weather data."
    )
    args_schema: Type[BaseModel] = WeatherToolInput

    def _run(self, location: str) -> str:
        """
        Get weather information for the specified location.

        Args:
            location: City name or location

        Returns:
            Weather information as a string
        """
        try:
            # Using Open-Meteo API (free, no API key required)
            # First, get coordinates for the location
            geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
            geo_response = requests.get(geocoding_url)
            geo_data = geo_response.json()

            if not geo_data.get('results'):
                return f"Could not find location: {location}"

            lat = geo_data['results'][0]['latitude']
            lon = geo_data['results'][0]['longitude']
            city_name = geo_data['results'][0]['name']
            country = geo_data['results'][0].get('country', '')

            # Get weather data
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&timezone=auto"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            current = weather_data['current']

            # Weather code interpretation (simplified)
            weather_codes = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Foggy",
                48: "Depositing rime fog",
                51: "Light drizzle",
                53: "Moderate drizzle",
                55: "Dense drizzle",
                61: "Slight rain",
                63: "Moderate rain",
                65: "Heavy rain",
                71: "Slight snow",
                73: "Moderate snow",
                75: "Heavy snow",
                95: "Thunderstorm",
            }

            weather_desc = weather_codes.get(current['weather_code'], "Unknown")

            result = f"""
Weather for {city_name}, {country}:
- Condition: {weather_desc}
- Temperature: {current['temperature_2m']}°C
- Feels like: {current['apparent_temperature']}°C
- Humidity: {current['relative_humidity_2m']}%
- Wind Speed: {current['wind_speed_10m']} km/h
- Precipitation: {current['precipitation']} mm
"""
            return result.strip()

        except Exception as e:
            return f"Error fetching weather data: {str(e)}"