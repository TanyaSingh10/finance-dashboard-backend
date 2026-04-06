from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.record import Record, RecordType
from app.schemas.record import DashboardSummary
from datetime import date

def get_dashboard_summary(db: Session) -> DashboardSummary:
    # aggregate income
    income_result = db.query(func.sum(Record.amount)).filter(
        Record.is_deleted == False, 
        Record.type == RecordType.income
    ).scalar()
    total_income = income_result or 0.0

    # aggregate expense
    expense_result = db.query(func.sum(Record.amount)).filter(
        Record.is_deleted == False, 
        Record.type == RecordType.expense
    ).scalar()
    total_expense = expense_result or 0.0

    net_balance = total_income - total_expense

    return DashboardSummary(
        total_income=total_income,
        total_expense=total_expense,
        net_balance=net_balance
    )

def get_category_totals(db: Session):
    results = db.query(
        Record.category, 
        func.sum(Record.amount).label("total")
    ).filter(
        Record.is_deleted == False
    ).group_by(Record.category).all()
    return [{"category": r[0], "total": r[1]} for r in results]
    
def get_monthly_trends(db: Session):
    results = db.query(
        func.strftime('%Y-%m', Record.date).label('month'),
        Record.type,
        func.sum(Record.amount).label('total')
    ).filter(
        Record.is_deleted == False
    ).group_by('month', Record.type).all()
    return [{"month": r[0], "type": r[1], "total": r[2]} for r in results]
