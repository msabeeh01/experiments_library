from fastapi import APIRouter, Body
from utils.spotipy import sp

router = APIRouter(
    prefix="/album",
)

@router.post("/search")
async def search_album(album: str = Body(embed=True)):
    # return info about album
    search = sp.search(album, type='album')
    return search

@router.get("/{album_id}")
async def get_album_info(album_id: str):
    # return info about album
    search = sp.album(album_id)
    return search 