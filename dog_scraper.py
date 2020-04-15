import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

webpage_response = requests.get(
    'https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&sex=A&agegroup=All&location=&site=&onhold=A&orderby=ID&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=xkrq0b4cx1bnywe67ehsy15rk2g3s5av66iy54jta0d27bomo7&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

dog_links = soup.select('.list-animal-name > a')
links = []

for a in dog_links:
    links.append(a['href'])

dog_data = {}

for link in links:
    webpage = requests.get(f'https://ws.petango.com/webservices/adoptablesearch/{link}')
    dog = BeautifulSoup(webpage.content, "html.parser")
    dog_name = dog.select("#lbName")[0].get_text()
    dog_stats = dog.find(attrs={'class': 'detail-table'})
    dog_stats_item = dog_stats.find_all('tr')
    dog_stats_list = []
    columns = []
    for item in dog_stats_item:
        columns.append(item.find(attrs={'class': 'detail-label'}).get_text().strip())
        dog_stats_value = item.find(attrs={'class': 'detail-value'}).get_text().strip()
        dog_stats_list.append(dog_stats_value)
    dog_data[dog_name] = dog_stats_list
pd.set_option("display.max_rows", None, "display.max_columns", None)
dog_df = pd.DataFrame.from_dict(dog_data, columns=columns, orient='index')
print(dog_df)

# dog_df.to_csv('dogs.csv')

# plt.hist(dog_df.Size)
# plt.show()
