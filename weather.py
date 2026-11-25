
import requests

def get_weather(city:str):
     
     """find the weather report for the given city.
                
                Args:
                    city : the given city name for which weather report to be fetched.
                    
             
    """
     API_KEY = "70c36ca4ab2c4b84952114302262011"

     url = "https://api.weatherapi.com/v1/current.json"

     params = {
        "key": API_KEY,
        "q": city,
        "aqi": "yes"
     }

     try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        current = data["current"]
        location = data["location"]

        print("\n===== WEATHER REPORT =====")
        print(f"City: {location['name']}")
        print(f"Country: {location['country']}")
        print(f"Temperature: {current['temp_c']} °C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Feels Like: {current['feelslike_c']} °C")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind Speed: {current['wind_kph']} km/h")

     except requests.exceptions.RequestException as e:
        print("API request error:", e)

     except KeyError:
        print("Unexpected API response")


# # Function call
# get_weather("New Delhi")
