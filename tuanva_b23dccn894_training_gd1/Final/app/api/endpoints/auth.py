from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models
from app.api.deps import get_db
from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import UserRole
from app.schemas.auth import LoginRequest, Token

router = APIRouter()


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Bootstrap a single admin account for now.
    if data.email == "admin" and data.password == "admin":
        user = db.query(models.User).filter(models.User.email == "admin").first()
        if not user:
            user = models.User(
                email="admin",
                full_name="admin",
                password=get_password_hash("admin"),
                role=UserRole.ADMIN,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        elif not verify_password(data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid credentials",
            )
    else:
        user = db.query(models.User).filter(models.User.email == data.email).first()
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid credentials",
            )
        # Enforce normal users to remain USER when logging in.
        if user.role != UserRole.USER:
            user.role = UserRole.USER
            db.commit()
            db.refresh(user)

    access_token = create_access_token(
        subject=str(user.id),
        role=user.role.value,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=access_token)
