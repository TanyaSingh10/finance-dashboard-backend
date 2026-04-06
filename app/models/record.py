import enum
from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, Enum, ForeignKey
from app.database.database import Base

class RecordType(str, enum.Enum):
    income = "income"
    expense = "expense"

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum(RecordType), nullable=False)
    category = Column(String, index=True, nullable=False)
    date = Column(Date, index=True, nullable=False, default=date.today)
    notes = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
