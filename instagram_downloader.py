import requests
from bs4 import BeautifulSoup as bs
import pyfiglet

header = pyfiglet.figlet_format("IG Downloader")
print(header)

ig_link = input('Paste link here:\n> ')
photo_id = ig_link.split('/')[4]
webpage_response = requests.get(ig_link)
webpage = webpage_response.content
soup = bs(webpage, "html.parser")
photo_link = soup.find(attrs={'property': 'og:image'})['content']
photo = requests.get(photo_link)

open(f'downloads_from_ig/{photo_id}.jpg', 'wb').write(photo.content)
