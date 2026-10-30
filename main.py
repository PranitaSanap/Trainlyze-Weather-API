
import requests
import os

# OpenWeather API Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    if not API_KEY:
        print("Error: API key not configured.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        print("\nFetching weather information...")

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("Error: City not found!")
            return

        if response.status_code == 401:
            print("Error: Invalid or inactive API key!")
            return

        response.raise_for_status()

        data = response.json()

        # Extract weather information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather = data["weather"][0]["description"]

        # Display weather report
        print("\n" + "=" * 40)
        print("       LIVE WEATHER REPORT")
        print("=" * 40)

        print(f"City          : {city_name}")
        print(f"Temperature   : {temperature} °C")
        print(f"Feels Like    : {feels_like} °C")
        print(f"Humidity      : {humidity}%")
        print(f"Wind Speed    : {wind_speed} m/s")
        print(f"Weather       : {weather}")

        print("=" * 40)
        print("Weather data fetched successfully!")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except (KeyError, IndexError):
        print("Error: Unexpected weather data received.")


# Main program
print("=" * 40)
print("       WEATHER INFORMATION SYSTEM")
print("=" * 40)

city = input("Enter city name: ").strip()

if city:
    get_weather(city)
else:
    print("Please enter a valid city name.")
