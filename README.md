# Weather App

A simple weather application that lets users search for a city and view current weather details such as temperature, humidity, wind speed, and weather condition.

This project includes:
- A front-end weather dashboard built with HTML, CSS, and JavaScript
- A Python script that fetches weather information from OpenWeatherMap
- Weather icons and a background theme for a polished UI

## Features

- Search weather by city name
- Display current temperature in Celsius
- Show humidity percentage
- Show wind speed
- Change weather icon based on conditions such as rain, clear sky, clouds, drizzle, mist, and snow
- Clean and responsive UI

## Project Structure

```text
Wether-app/
├── Backend.py
├── Background.css
├── index.html
├── wallpaper.png
├── wallpaper2.png
├── images/
│   ├── clear.png
│   ├── clouds.png
│   ├── drizzle.png
│   ├── humidity.png
│   ├── mist.png
│   ├── rain.png
│   ├── search.png
│   ├── snow.png
│   └── wind.png
└── README.md
```

## Tech Stack

- HTML
- CSS
- JavaScript
- Python
- OpenWeatherMap API

## Requirements

Before running the app, make sure you have:

- A modern web browser
- Python 3 installed
- Internet connection
- An OpenWeatherMap API key

## Getting Started

### 1. Open the web app

Open the `index.html` file directly in a browser or run a local server:

```bash
cd path/to/Wether-app
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

### 2. Run the Python script

The Python file `Backend.py` can also be used to get weather details in the terminal:

```bash
cd path/to/Wether-app
python Backend.py
```

When prompted, enter a city name.

## API Configuration

This app uses the OpenWeatherMap API. Store your API key as a local environment variable instead of committing it to source control.

### JavaScript

In `index.html`, replace the placeholder with your own key:

```javascript
const apikey = "YOUR_OPENWEATHERMAP_API_KEY";
```

### Python

In `Backend.py`, set the environment variable before running the app:

```bash
set OPENWEATHER_API_KEY=your_api_key_here
```

```python
api_key = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHERMAP_API_KEY")
```

## Notes

- The app fetches live weather data from OpenWeatherMap.
- API keys should not be committed publicly if used in a production environment.
- If a city is not found, the app shows an error message.
- The project can be extended with features like:
  - 5-day forecast
  - temperature conversion
  - location-based weather detection
  - dark/light theme toggle

## License

This project is for educational and personal use.
