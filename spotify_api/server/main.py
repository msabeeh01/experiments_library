from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# spotipy imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# dotenv imports
from dotenv import load_dotenv
import os

load_dotenv()

# cors allowed origins
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client_id=os.getenv('CLIENT_ID')
client_secret=os.getenv('CLIENT_SECRET')

# spotipy client
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


@app.get("/{artist}")
async def root(artist: str):
    # return info about album
    search = sp.search(artist, type='artist')
    return search