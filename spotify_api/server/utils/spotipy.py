# spotipy imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# dotenv imports
from dotenv import load_dotenv
import os

load_dotenv()

#spoipy setup
client_id=os.getenv('CLIENT_ID')
client_secret=os.getenv('CLIENT_SECRET')

# spotipy client
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)