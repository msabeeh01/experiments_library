# spotipy imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# dotenv imports
from dotenv import load_dotenv
import os

load_dotenv()

#spoipy setup
client_id=os.getenv('CLIENT_ID')
client_secret=os.getenv('CLIENT_SECRET')
scope = 'user-top-read user-read-private user-read-recently-played'
redirect_uri='http://localhost:3000'

# spotipy client
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=auth_manager)