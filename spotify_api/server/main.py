from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import Annotated

#router imports
from utils.spotipy import sp
from album import router as album_router

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

app.include_router(album_router)

@app.get("/login")
def login():
    return sp.user()

@app.get("/top")
def get_playlists():
    return sp.current_user_top_tracks()

@app.get("/recent")
def get_recently_played():
    return sp.current_user_recently_played()


from utils.utility import get_hashed_password, verify_password

@app.post("/pwd")
async def hash_pwd(password: str = Body(embed=True)):
    # return hashed password
    hashed = get_hashed_password(password)
    return hashed


@app.post("/pwd/verify")
async def verify_pwd(password: str = Body(embed=True), hashed_password: str = Body(embed=True)):
    # return hashed password
    return verify_password(password, hashed_password)