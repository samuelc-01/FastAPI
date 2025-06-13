from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Samuel",
        last_name="Cristian",
        gender=Gender.male,
        roles=[Role.student]      
    ),
    User(
        id=uuid4(),
        first_name="Jean",
        last_name="Cristian",
        gender=Gender.male,
        roles=[Role.admin, Role.user]      
    ),
]

@app.get("/")
def root():
    return {"Hello": "Word"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;