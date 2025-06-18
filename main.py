from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import User, Gender, Role, UserUpdateRequest

#py -m uvicorn main:app --reload
#lh:yourport/docs for swagger
#lh:your    port/redoc for documation created by swagger

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


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

# start next commit