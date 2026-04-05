from fastapi import HTTPException
from database import SessionLocal
from models_db import UserDB

def get_user(user_id: int):
    db = SessionLocal()

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.active:
        raise HTTPException(status_code=403, detail="User inactive")

    return user


def check_permission(user, action):
    role = user.role

    if role == "admin":
        return True

    if role == "analyst" and action in ["read", "create"]:
        return True

    if role == "viewer" and action == "read":
        return True

    raise HTTPException(status_code=403, detail="Access denied")