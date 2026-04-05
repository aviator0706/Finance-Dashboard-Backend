from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    active = Column(Boolean, default=True)


class RecordDB(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    note = Column(String)
    deleted = Column(Boolean, default=False)