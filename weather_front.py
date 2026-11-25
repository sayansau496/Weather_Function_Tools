
import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Weather Application",
    page_icon="🌤️",
    layout="centered"
)

# Weather Function
def get_weather(city: str) -> dict:

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


# ---------------- FRONTEND ----------------

st.title("🌤️ Weather Application")

st.write("Check the current weather of any city in the world.")

st.divider()

# City Input
city = st.text_input(
    "Enter City Name",
    placeholder="Example: Kolkata, Mumbai, London"
)

# Search Button
if st.button("Get Weather", use_container_width=True):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:

        with st.spinner("Fetching weather information..."):

            result = get_weather(city.strip())

        if "error" in result:

            st.error(result["error"])

        else:

            st.success(
                f"Weather Report: {result['city']}, "
                f"{result['country']}"
            )

            st.subheader(
                f"🌡️ {result['temperature']} °C"
            )

            st.write(
                f"**Condition:** {result['condition']}"
            )

            st.divider()

            # Display Weather Details
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Feels Like",
                    f"{result['feels_like']} °C"
                )

                st.metric(
                    "Humidity",
                    f"{result['humidity']}%"
                )

            with col2:
                st.metric(
                    "Wind Speed",
                    f"{result['wind_speed']} km/h"
                )

            st.divider()

            st.caption(
                "Weather information powered by WeatherAPI"
            )
