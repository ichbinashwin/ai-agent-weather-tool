from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from tools.weather_tool import get_weather
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Weather Tool API",
    description="API for fetching current weather using OpenWeatherMap",
    version="1.0.0"
)

# Optional: Allow frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/weather", summary="Get current weather", tags=["Weather"])
def weather(city: str = Query(..., description="City to get the weather for")):
    """
    Returns the current weather in a given city.
    """
    result = get_weather(city)
    return {"result": result}

