from sqlalchemy.orm import Session
from app.models.record import Record, RecordType
from app.schemas.record import RecordCreate, RecordUpdate
from datetime import date
from typing import Optional

def create_record(db: Session, record: RecordCreate, user_id: int):
    db_record = Record(**record.model_dump(), user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None, 
    category: Optional[str] = None,
    record_type: Optional[RecordType] = None
):
    query = db.query(Record).filter(Record.is_deleted == False)

    if start_date:
        query = query.filter(Record.date >= start_date)
    if end_date:
        query = query.filter(Record.date <= end_date)
    if category:
        query = query.filter(Record.category == category)
    if record_type:
        query = query.filter(Record.type == record_type)

    return query.order_by(Record.date.desc()).offset(skip).limit(limit).all()

def get_record(db: Session, record_id: int):
    return db.query(Record).filter(Record.id == record_id, Record.is_deleted == False).first()

def update_record(db: Session, db_record: Record, record_update: RecordUpdate):
    update_data = record_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_record, key, value)
    
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def delete_record(db: Session, db_record: Record):
    db_record.is_deleted = True
    db.add(db_record)
    db.commit()
    return db_record
