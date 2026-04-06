from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.record import RecordType

class RecordBase(BaseModel):
    amount: float
    type: RecordType
    category: str
    date: date
    notes: Optional[str] = None

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[RecordType] = None
    category: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None

class Record(RecordBase):
    id: int
    user_id: Optional[int] = None

    class Config:
        from_attributes = True

class DashboardSummary(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float
