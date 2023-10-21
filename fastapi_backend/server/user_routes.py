from fastapi import APIRouter, Body
from pydantic import BaseModel, EmailStr

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

@router.post("/add")
async def add_user(user: User = Body(...)):
    r.set(user.user, user.email)
    return r

