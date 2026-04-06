from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.database.database import get_db
from app.schemas.record import Record, RecordCreate, RecordUpdate
from app.models.record import RecordType
from app.models.user import User
from app.services import record as record_service
from app.core.deps import require_analyst

router = APIRouter(prefix="/records", tags=["records"])

@router.post("/", response_model=Record, status_code=201)
def create_record(
    record: RecordCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_analyst)
):
    return record_service.create_record(db=db, record=record, user_id=current_user.id)

@router.get("/", response_model=List[Record])
def read_records(
    skip: int = 0,
    limit: int = 100,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    category: Optional[str] = None,
    type: Optional[RecordType] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_analyst)
):
    return record_service.get_records(
        db, skip=skip, limit=limit, 
        start_date=start_date, end_date=end_date, 
        category=category, record_type=type
    )

@router.put("/{record_id}", response_model=Record)
def update_record(
    record_id: int, 
    record_update: RecordUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_analyst)
):
    db_record = record_service.get_record(db, record_id=record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record_service.update_record(db, db_record, record_update)

@router.delete("/{record_id}")
def delete_record(
    record_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_analyst)
):
    db_record = record_service.get_record(db, record_id=record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    record_service.delete_record(db, db_record)
    return {"detail": "Record deleted"}
