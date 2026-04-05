from fastapi import APIRouter, HTTPException
from models import Record
from database import SessionLocal
from models_db import RecordDB
from utils.auth import get_user, check_permission
from typing import Optional

router = APIRouter()


# SEARCH
@router.get("/records/search")
def search_records(user_id: int, keyword: str):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()

    results = db.query(RecordDB).filter(
        RecordDB.note.ilike(f"%{keyword}%"),
        RecordDB.deleted == False
    ).all()

    return {"results": results}


# CREATE
@router.post("/records")
def create_record(record: Record, user_id: int):
    user = get_user(user_id)
    check_permission(user, "create")

    db = SessionLocal()

    new_record = RecordDB(**record.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {"message": "Record created", "data": new_record}


# GET (filter + pagination)
@router.get("/records")
def get_records(
    user_id: int,
    type: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()

    query = db.query(RecordDB).filter(RecordDB.deleted == False)

    if type:
        query = query.filter(RecordDB.type == type)

    if category:
        query = query.filter(RecordDB.category == category)

    records = query.offset(offset).limit(limit).all()

    return {"records": records}


# UPDATE
@router.put("/records/{record_id}")
def update_record(record_id: int, updated_record: Record, user_id: int):
    user = get_user(user_id)
    check_permission(user, "update")

    db = SessionLocal()

    record = db.query(RecordDB).filter(RecordDB.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail=f"Record with id {record_id} not found")

    record.amount = updated_record.amount
    record.type = updated_record.type
    record.category = updated_record.category
    record.date = updated_record.date
    record.note = updated_record.note

    db.commit()

    return {"message": "Record updated successfully"}


# SOFT DELETE
@router.delete("/records/{record_id}")
def delete_record(record_id: int, user_id: int):
    user = get_user(user_id)
    check_permission(user, "delete")

    db = SessionLocal()

    record = db.query(RecordDB).filter(RecordDB.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    record.deleted = True
    db.commit()

    return {"message": "Record soft deleted"}