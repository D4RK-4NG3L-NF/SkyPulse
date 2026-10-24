import os

import requests

api_key = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHERMAP_API_KEY")
city = input("Enter city: ").strip()

if not city:
    print("City name cannot be empty.")
    raise SystemExit(1)

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&units=metric&appid={api_key}"
)
response = requests.get(url, timeout=10)
weather_data = response.json()

if response.status_code == 404 or weather_data.get("cod") == 404:
    print("No city found")
else:
    weather = weather_data["weather"][0]["main"]
    temp = weather_data["main"]["temp"]

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}°C")
