from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.user import User, UserRole
from app.schemas.user import UserCreate
from app.services.user import create_user

def init_db():
    db = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == "admin").first()
        if not admin_user:
            user_in = UserCreate(
                username="admin",
                email="admin@example.com",
                password="admin",
                role=UserRole.admin
            )
            create_user(db, user_in)
            print("Created default admin user: admin / admin")
    finally:
        db.close()
