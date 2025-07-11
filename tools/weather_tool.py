# Tool Name: Weather
#from langchain.tools import tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

#@tool
def get_weather(city: str) -> str:
    """Get current weather for a given city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather is {city} is {weather} with {temp}°C."
    except Exception as e:
        return f"Could not retrieve weather data for {city}. Error: {str(e)}"

