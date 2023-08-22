import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import ast

load_dotenv()

CLIENT_ID = os.getenv("id")
CLIENT_SECRET = os.getenv("key")
REDIRECT_URL = 'http://example.com'

#---------------------Brain-of-operation------------#
class Brain:
    def __init__(self) -> None:
        # try:
        #     os.remove(".cache")
        # except FileNotFoundError:
        #     pass
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri="http://example.com",
                                                    scope="playlist-modify-private"))
        self.user_key = self.sp.current_user()["id"]

        with open(".cache","r") as file:
           self.auth = ast.literal_eval(file.read())['access_token']
        print(self.sp.search(q=f"track:Only-Human-year:2022-02-02 ", type="track"))

              
            
                



Brain()