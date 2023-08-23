import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

CLIENT_ID = os.getenv("id")
CLIENT_SECRET = os.getenv("key")
REDIRECT_URL = 'http://example.com'
ENDPOINT = 'https://api.spotify.com/v1/search'

#---------------------Auth-token-generator------------#
class Auth:
    def __init__(self) -> None:
        try:
            os.remove(".cache")
        except FileNotFoundError:
            pass
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri="http://example.com",
                                                    scope=" playlist-modify-public"))
        self.user_key = self.sp.current_user()["id"]


