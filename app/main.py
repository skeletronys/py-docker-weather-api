import os
import requests

CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API_KEY environment variable not set.")
        return

    url = (f"http://api.openweathermap.org/data/2.5/weather?"
           f"q={CITY}&appid={api_key}&units=metric")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"Weather in {CITY}: {weather.capitalize()}, {temp}°C")
    else:
        print(f"Error: {data['message']}")


if __name__ == "__main__":
    get_weather()
