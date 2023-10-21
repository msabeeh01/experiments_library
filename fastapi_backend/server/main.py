from typing import Union
from fastapi import FastAPI

from user_routes import router as user_router

# redis import
from redis_client import r

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
