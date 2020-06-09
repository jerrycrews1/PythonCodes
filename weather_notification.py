import requests
import os
import smtplib
from email.mime.text import MIMEText


def get_zip():
    while True:
        try:
            zip_code = int(input("Enter zip code: "))
            if len(str(zip_code)) != 5:
                raise TypeError
            else:
                break
        except (TypeError, ValueError):
            print("Please enter a valid 5-digit zip code.")
            continue
    return zip_code


def send_mail(message, day):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    msg = MIMEText(message)
    sender = ''
    recipients = ['', '']
    msg['Subject'] = f"Weather {day}"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    server.login(sender, PASSWORD)
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()


def get_current_weather():
    zip_code = get_zip()
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={APIKEY}&q={zip_code}')
    data = response.json()
    description = data['current']['condition']['text']
    temp = data['current']['temp_f']
    city_name = data['location']['name']
    inside_message = f"{description} and {round(temp)}\N{DEGREE SIGN}F in {city_name}."
    send_mail(inside_message)


def get_tomorrow_weather():
    zip_code = get_zip()
    response = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={APIKEY}&q={zip_code}&days=1')
    data = response.json()
    high_temp = data['forecast']['forecastday'][0]['day']['maxtemp_f']
    low_temp = data['forecast']['forecastday'][0]['day']['mintemp_f']
    description = data['forecast']['forecastday'][0]['day']['condition']['text'].lower()
    city_name = data['location']['name']
    inside_message = f'Tomorrow in {city_name} the weather is {description} with a high of {high_temp}' \
                     f'\N{DEGREE SIGN}F and a low of {low_temp}\N{DEGREE SIGN}F'
    send_mail(inside_message)


def get_today_weather():
    zip_code = '22003'
    response = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={APIKEY}&q={zip_code}&days=2')
    data = response.json()
    high_temp = data['forecast']['forecastday'][0]['day']['maxtemp_f']
    low_temp = data['forecast']['forecastday'][0]['day']['mintemp_f']
    description = data['forecast']['forecastday'][0]['day']['condition']['text'].lower()
    city_name = data['location']['name']
    inside_message = f'Today in {city_name} the weather is {description} with a high of {round(high_temp)}' \
                     f'\N{DEGREE SIGN}F and a low of {round(low_temp)}\N{DEGREE SIGN}F'
    send_mail(inside_message, "Today")


get_today_weather()
