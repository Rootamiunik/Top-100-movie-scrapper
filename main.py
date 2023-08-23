import os
from dotenv import load_dotenv
from auth import Auth
from brain import Brain
import ast
import spotipy

#--------------main-----------------#


date = input("Playlist of Top 100 songs of date (YYYY-MM-DD):  ")

brain = Brain(date)
brain.create_playlist() #creates playlist
brain.add_songs() #adds song