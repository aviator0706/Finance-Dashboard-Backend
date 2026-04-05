from fastapi import FastAPI
from routes import users, records, dashboard
from database import engine, Base
import models_db

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Finance Dashboard Backend")

app.include_router(users.router)
app.include_router(records.router)
app.include_router(dashboard.router)

@app.get("/")
def home():
    return {
        "message": "Hello, I'm Avi Alok, 3rd Year IT Student at IIEST Shibpur",
        "project": "Finance Dashboard Backend",
        "description": "This backend supports user roles, financial records, dashboard analytics, and access control.",
        "features": [
            "User management (Admin, Analyst, Viewer)",
            "CRUD operations for financial records",
            "Role-based access control",
            "Dashboard analytics (summary, category, trends)",
            "Search, pagination, soft delete",
            "SQLite database persistence"
        ],
        "note": "Visit /docs to explore all APIs"
    }