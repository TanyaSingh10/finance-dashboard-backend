from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Finance Dashboard API"
    SECRET_KEY: str = "super_secret_temporary_key_replace_me_in_prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    DATABASE_URL: str = "sqlite:///./finance_dashboard.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
