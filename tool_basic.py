
import os
import requests

def get_weather(city: str) -> dict:
    """
    Find the current weather report for the given city.

    Args:
        city: City name for which weather information is required.

    Returns:
        Dictionary containing weather information.
    """

    API_KEY = "70c36ca4ab2c4b84952114302262011"

    if not API_KEY:
        return {"error": "Weather API key is missing"}

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "yes"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]
        location = data["location"]

        weather_report = {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temp_c"],
            "condition": current["condition"]["text"],
            "feels_like": current["feelslike_c"],
            "humidity": current["humidity"],
            "wind_speed": current["wind_kph"]
        }

        return weather_report

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

    except (KeyError, TypeError):
        return {"error": "Unexpected API response"}


# Function call
result = get_weather("Kolkata")

print(result)
