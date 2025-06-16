from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import User, Gender, Role

#py -m uvicorn main:app --reload
#lh:yourport/docs for swagger
#lh:yourport/redoc for documation created by swagger
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("12fd9054-1b1e-4d55-99b9-2089a5c9b1fd"),
        first_name="Samuel",
        last_name="Cristian",
        gender=Gender.male,
        roles=[Role.student]      
    ),
    User(
        id=UUID("dcefb1c3-c092-4b66-a1c8-570139f783b4"),
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

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
# start next commit