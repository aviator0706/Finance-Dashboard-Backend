from fastapi import APIRouter
from models import User
from database import SessionLocal
from models_db import UserDB

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    db = SessionLocal()

    new_user = UserDB(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "data": {
        "id": new_user.id,
        "name": new_user.name,
        "role": new_user.role,
        "active": new_user.active
    }}


@router.get("/users")
def get_users():
    db = SessionLocal()

    users = db.query(UserDB).all()

    return {"users": users}