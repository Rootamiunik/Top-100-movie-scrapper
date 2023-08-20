import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
html_data = requests.get(url=URL).text
soup = BeautifulSoup(html_data,'html.parser')
data = soup.find_all(name='h3',class_='listicleItem_listicle-item__title__hW_Kn')

for i in data[::-1]:
    with open('movie.txt',"a") as file:
        file.write(f"{i.getText()}\n")

