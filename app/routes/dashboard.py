from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.record import DashboardSummary
from app.models.user import User
from app.services import dashboard as dashboard_service
from app.core.deps import require_viewer

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary", response_model=DashboardSummary)
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_viewer)
):
    return dashboard_service.get_dashboard_summary(db)

@router.get("/category-totals")
def get_category_totals(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_viewer)
):
    return dashboard_service.get_category_totals(db)

@router.get("/monthly-trends")
def get_monthly_trends(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_viewer)
):
    return dashboard_service.get_monthly_trends(db)
