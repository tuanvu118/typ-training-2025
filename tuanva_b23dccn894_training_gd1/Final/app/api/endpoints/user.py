from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_admin, require_self_or_admin
from app.core.security import get_password_hash
from app.models.user import UserRole
from app.schemas.user import User, UserCreate, UserUpdate
from app import models

router=APIRouter()

@router.get("/",response_model=List[User])
def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin),
):
    """get list of users,pagination supported"""
    user=db.query(models.User).offset(skip).limit(limit).all()
    return user

@router.get("/{user_id}",response_model=User)
def get_user(
    user_id:int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_self_or_admin),
):
    """ get details of a user by ID"""
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user

@router.post("/",response_model=User,status_code=status.HTTP_201_CREATED)
def create_user(
       user_in: UserCreate,
       db: Session=Depends(get_db)
):
    """ create new user and check unique email"""
    existing=db.query(models.User).filter(models.User.full_name==user_in.full_name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this full name already exists"
        )
    user_data = user_in.dict()
    user_data["password"] = get_password_hash(user_data["password"])
    user_data["role"] = UserRole.USER
    db_user = models.User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/{user_id}",response_model=User)
def update_user(
    user_id:int,
    user_in:UserUpdate,
    db:Session=Depends(get_db),
    current_user: models.User = Depends(require_self_or_admin),
):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    if user_in.full_name is not None and user_in.full_name != user.full_name:
        existing=db.query(models.User).filter(models.User.full_name == user_in.full_name).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this full name already exists"
            )
    update_data = user_in.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = get_password_hash(update_data["password"])
    for field, value in update_data.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user
