import requests
from data import Data
from auth import Auth
import ast
import pprint

ENDPOINT = 'https://api.spotify.com/v1'

class Brain():
    def __init__(self,input_) -> None:
        self.input_ = input_
        self.data_obj = Data(input_=self.input_) #? Data creation
        self.auth = Auth() #? Creates a auth token
        self.data_list = self.data_obj.get_list()
        self.url_list = []
        self.pp = pprint.PrettyPrinter(indent=4)

        with open(".cache","r") as file:
           self.auth = ast.literal_eval(file.read())['access_token']
        
        self.header = {
            'Authorization': f'Bearer {self.auth}' ,
        }

        #------------user-id-and-playlist-id-generator-----------#
        self.user_id_genetator()
        self.songs_url_collector()

#-------------------Collects-the-uri-of-each-songs--------------------------#
    def songs_url_collector(self):
        self.search_endpoint = f"{ENDPOINT}/search"
        for i in range(len(self.data_list)):
            self.parms = {
                'q': f'track: {self.data_list[i]} year: {input}',
                'type': 'track',
                'limit':'10',
            }
            try:
                server_req = requests.get(url=self.search_endpoint,headers=self.header,timeout=120,params=self.parms)
                server_req.raise_for_status()
                self.url = server_req.json()['tracks']['items'][0]['uri']
                self.url_list.append(self.url)
            except IndexError:
                pass

#----------------Generates-user-id----------------------#
    def user_id_genetator(self):
        self.user_id_endpoint = f"{ENDPOINT}/me"
        server_req = requests.get(url=self.user_id_endpoint,headers=self.header,timeout=120)
        self.user_id = server_req.json()['id']
         
#-------------------Creates_a_new_playllist--------------------#
    def create_playlist(self):
        self.playlist_endpoint = f"{ENDPOINT}/users/{self.user_id}/playlists"

        header = {
            'Authorization': f'Bearer {self.auth}' ,
            'user_id':self.user_id,
        }

        self.playlist_parms = {
            'name':f'{self.input_} Billboard 100',
            'public':"true",
            'description':f"The top 100 song of {self.input_}"
        }

        server_post_req = requests.post(url=self.playlist_endpoint,headers=header,timeout=120,json=self.playlist_parms)
        server_post_req.raise_for_status()

#---------------Song adder-------------------#
    def add_songs(self):
        self.playlist_add_endpoint = f'{ENDPOINT}/playlists/{self.playlist_id_generator()}/tracks'

        header = {
            'Authorization': f'Bearer {self.auth}' ,
            'playlist_id':self.playlist_id_generator(),
        }

        playlist_parms = {
            'uris':self.url_list,
            'position': 0,
            
        }

        server_post_req = requests.post(url=self.playlist_add_endpoint,headers=header,timeout=120,json=playlist_parms)
        
       

#---------------Playlist-id-generator--------------#
    def playlist_id_generator(self):
        header = {
            'Authorization': f'Bearer {self.auth}' ,
            'user_id':self.user_id,

           }

        self.playlist_id_endpoint =f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        
        server_req = requests.get(url=self.playlist_id_endpoint,headers=header,timeout=120)
        server_req.raise_for_status()
        self.raw_data_for_playlist_id = server_req.json()['items']
        for i in range(len(self.raw_data_for_playlist_id)):
            if self.raw_data_for_playlist_id[0]['name'] == f'{self.input_} Billboard 100':
                return self.raw_data_for_playlist_id[i]['id']

        
            
              
