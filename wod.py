import datetime
from bs4 import BeautifulSoup
import requests


def get_wod():
    year = str(datetime.datetime.now().year)[:2]
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    if len(day) < 2:
        day = str(0) + day
    if len(month) < 2:
        month = str(0) + month
    date_in_crossfit_format = f"{year}{month}{day}"
    url = f'https://www.crossfit.com/{date_in_crossfit_format}'
    webpage = requests.get(url)
    webpage_content = webpage.content
    soup = BeautifulSoup(webpage_content, 'html.parser')
    wod = soup.select('div > article')[0]
    return wod


print(get_wod())
