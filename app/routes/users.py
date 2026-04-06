from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.schemas.user import User, UserCreate, UserUpdate
from app.services import user as user_service
from app.core.deps import require_admin

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User, dependencies=[Depends(require_admin)])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return user_service.create_user(db=db, user=user)

@router.get("/", response_model=List[User], dependencies=[Depends(require_admin)])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users

@router.put("/{user_id}", response_model=User, dependencies=[Depends(require_admin)])
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.update_user(db, db_user, user_update)
