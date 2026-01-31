from sqlalchemy import create_engine # Tạo “engine” kết nối tới database
from sqlalchemy.orm import sessionmaker # Tạo “session” để tương tác với database

from app.core.config import settings

engine=create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)