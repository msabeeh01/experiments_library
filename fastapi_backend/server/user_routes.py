from fastapi import APIRouter, Body
from pydantic import BaseModel, EmailStr
import json

from supabase_client import supabase

router = APIRouter(
    prefix = "/users",
)

from redis_client import r

# user model
class User(BaseModel):
    user: str
    email: str

@router.get("/")
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]

@router.get("/pets")
async def get_pets():
    response = supabase.table("pets").select("*").execute()
    
    
    # check if redis has same data, return data as json
    if r.exists("pets"):
        print("redis")
        data = r.get("pets")
        return json.loads(data)
    
    # add data to redis
    responseString = json.dumps(response.data)
    r.set("pets", responseString)
    return response.data

@router.post("/add")
async def add_user(user: User = Body(...)):
    r.set(user.user, user.email)
    return r

