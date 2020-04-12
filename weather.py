import requests
import os

APIKEY = os.environ['APIKEY']


def kelvin_to_fahrenheit(temp):
    new_temp = 9/5 * (temp - 273) + 32
    return new_temp


def get_current_weather():
    good_zip = False
    while not good_zip:
        try:
            zip_code = int(input("Enter zip code: "))
            if len(str(zip_code)) != 5:
                raise TypeError
            else:
                break
        except (TypeError, ValueError):
            print("Please enter a valid 5-digit zip code.")
            continue
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={APIKEY}")
    data = response.json()
    temp = kelvin_to_fahrenheit(data['main']['temp'])
    city_name = data['name']
    return print(f"The current temperature in {city_name} is {round(temp)}\N{DEGREE SIGN}F")


get_current_weather()
