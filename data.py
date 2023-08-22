import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100'

class Data:
    def __init__(self,input_:str) -> None:
        #---------Request-data------------#
        self.formated_url = f"{URL}/{input_}/"
        self.server_response = requests.get(url=self.formated_url).text
        self.soup = BeautifulSoup(self.server_response,'html.parser')

    
    def get_list(self):
        #----------------processed/formated-data---------------#
        self.raw_data = self.soup.select(selector="div .o-chart-results-list-row-container ul li h3 ")
        return [i.getText().strip() for i in self.raw_data]

        

