# 🌤️ Weather Application

A simple and interactive **Weather Application** developed using Python and Streamlit. This application allows users to check the current weather conditions of any city around the world using the WeatherAPI.

## 🚀 Project Overview

The Weather Application fetches real-time weather information based on the city entered by the user. It displays temperature, weather conditions, humidity, wind speed, and feels-like temperature through an easy-to-use web interface.

## ✨ Features

- 🌍 Search weather information for any city worldwide.
- 🌡️ Display current temperature in Celsius.
- ☁️ Show current weather conditions.
- 🌡️ Display feels-like temperature.
- 💧 Show humidity percentage.
- 💨 Display wind speed in km/h.
- ⚡ Real-time weather data using WeatherAPI.
- 🎨 Interactive and user-friendly Streamlit interface.
- 🛡️ Error handling for invalid city names and API connection issues.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application frontend |
| Requests | API communication |
| WeatherAPI | Real-time weather information |

## 📁 Project Structure

```text
Weather-Application/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Weather-Application.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Weather-Application
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Configure WeatherAPI

1. Visit https://www.weatherapi.com/
2. Create a free account.
3. Generate your API key.
4. Add the API key securely to your application.

For better security, use Streamlit secrets instead of hardcoding the API key.

Create a `.streamlit/secrets.toml` file:

```toml
WEATHER_API_KEY = "your_api_key"
```

Update the API key line in `app.py`:

```python
API_KEY = st.secrets["WEATHER_API_KEY"]
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 📊 Weather Information Displayed

| Parameter | Description |
|---|---|
| City | Selected city name |
| Country | Country name |
| Temperature | Current temperature in °C |
| Condition | Current weather condition |
| Feels Like | Feels-like temperature in °C |
| Humidity | Humidity percentage |
| Wind Speed | Wind speed in km/h |

## 🖥️ Application Workflow

1. Open the Weather Application.
2. Enter a city name in the input field.
3. Click on the **Get Weather** button.
4. The application sends a request to WeatherAPI.
5. WeatherAPI returns the current weather information.
6. The application displays the weather report.

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```text
streamlit
requests
```

## 🔮 Future Enhancements

- Add a 7-day weather forecast.
- Display weather icons and images.
- Add sunrise and sunset information.
- Include air quality information.
- Add temperature conversion (Celsius/Fahrenheit).
- Add weather information for multiple cities.
- Deploy the application using Streamlit Community Cloud.

## 👨‍💻 Author

**Developed by:** Sayan Sau

**Project:** Python – Streamlit Weather Application

## 📄 License

This project is created for educational and learning purposes.

---

⭐ Special Thanks to 
Mr Amitava Chattopadhyay Sir and Mrs Arpita Gupta Madam (CoE Kolkata)
