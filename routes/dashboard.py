from fastapi import APIRouter
from database import SessionLocal
from models_db import RecordDB
from utils.auth import get_user, check_permission

router = APIRouter()

# SUMMARY
@router.get("/dashboard/summary")
def get_summary(user_id: int):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()
    records = db.query(RecordDB).filter(RecordDB.deleted == False).all()

    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }


# CATEGORY
@router.get("/dashboard/category")
def category_summary(user_id: int):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()
    records = db.query(RecordDB).filter(RecordDB.deleted == False).all()

    result = {}

    for r in records:
        result[r.category] = result.get(r.category, 0) + r.amount

    return result


# RECENT
@router.get("/dashboard/recent")
def recent_transactions(user_id: int):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()
    records = db.query(RecordDB).filter(RecordDB.deleted == False).all()

    sorted_records = sorted(records, key=lambda x: str(x.date), reverse=True)

    return {"recent": sorted_records[:5]}


# MONTHLY
@router.get("/dashboard/monthly")
def monthly_trends(user_id: int):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()
    records = db.query(RecordDB).filter(RecordDB.deleted == False).all()

    result = {}

    for r in records:
        month = str(r.date)[:7]   # SAFE

        if month not in result:
            result[month] = {"income": 0, "expense": 0}

        if r.type == "income":
            result[month]["income"] += r.amount
        else:
            result[month]["expense"] += r.amount

    return result


# WEEKLY
@router.get("/dashboard/weekly")
def weekly_trends(user_id: int):
    user = get_user(user_id)
    check_permission(user, "read")

    db = SessionLocal()
    records = db.query(RecordDB).filter(RecordDB.deleted == False).all()

    result = {}

    for r in records:
        week = str(r.date)[:10]  # simplified week grouping

        if week not in result:
            result[week] = {"income": 0, "expense": 0}

        if r.type == "income":
            result[week]["income"] += r.amount
        else:
            result[week]["expense"] += r.amount

    return result