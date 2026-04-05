# 💰 Finance Dashboard Backend

## 📌 Overview

This project is a backend system for managing financial records with role-based access control and dashboard analytics.

It is designed to demonstrate backend development concepts such as API design, data modeling, validation, access control, and data persistence.

---

## 🚀 Features

### 👤 User & Role Management

* Create and manage users
* Roles supported: **Admin, Analyst, Viewer**
* Active/inactive user handling

### 🔐 Role-Based Access Control (RBAC)

* Admin → Full access (CRUD + management)
* Analyst → Read + Create access
* Viewer → Read-only access
* Permissions enforced at backend level

---

### 💰 Financial Records Management

* Create, Read, Update, Delete records
* Fields:

  * Amount
  * Type (income / expense)
  * Category
  * Date
  * Note
* Filtering by:

  * Type
  * Category

---

### 🔍 Search Functionality

* Keyword-based search on:

  * Note
  * Category

---

### 📦 Pagination

* Supports `limit` and `offset`
* Efficient handling of large datasets

---

### 🗑️ Soft Delete

* Records are not permanently deleted
* Marked as `deleted = True`
* Prevents data loss and allows recovery

---

### 📊 Dashboard Analytics

* Total income
* Total expense
* Net balance
* Category-wise summary
* Recent transactions
* Monthly trends
* Weekly trends

---

### ✅ Validation & Error Handling

* Input validation using **Pydantic**
* Proper HTTP status codes:

  * 400 → Bad request
  * 403 → Unauthorized
  * 404 → Not found
* Clear and meaningful error messages

---

### 🗄️ Data Persistence

* SQLite database using **SQLAlchemy ORM**
* Data persists across server restarts

---

## 🛠️ Tech Stack

* **FastAPI** (Backend framework)
* **SQLAlchemy** (ORM)
* **SQLite** (Database)
* **Pydantic** (Validation)

---

## 🧱 Project Structure

```
project/
│
├── main.py
├── models.py          # Pydantic models (validation)
├── models_db.py       # SQLAlchemy models (database)
├── database.py        # DB configuration
│
├── routes/
│   ├── users.py
│   ├── records.py
│   └── dashboard.py
│
├── utils/
│   └── auth.py        # RBAC logic
```

---

## ⚙️ How to Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

Open Swagger UI:
👉 http://127.0.0.1:8000/docs

---

## 🔄 Request Flow

Client → API Route → Pydantic Validation →
Authorization Check → Database Query → Response

---

## 🧠 Design Decisions

* **FastAPI** chosen for simplicity and automatic validation
* **SQLite** used for lightweight persistence
* **SQLAlchemy ORM** used for clean database interaction
* **RBAC implemented in backend** for security
* **Modular structure** for maintainability

---

## ⚖️ Trade-offs

* Authentication simplified using `user_id` instead of JWT
* SQLite used instead of PostgreSQL for simplicity
* Focus kept on backend logic rather than deployment

---

## 📌 Assumptions

* User identity is passed using `user_id` (no login system)
* Designed for demonstration and evaluation purposes

---

## 🚀 Future Improvements

* JWT-based authentication
* PostgreSQL / MongoDB integration
* API rate limiting
* Unit and integration testing
* Deployment (Render / AWS)

---

## 🎯 Conclusion

This project demonstrates core backend engineering skills including:

* API design
* Database interaction
* Role-based access control
* Validation and error handling
* Data processing and analytics

---
