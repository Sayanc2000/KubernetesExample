import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.oauth2 import get_password_hash, get_current_active_user
from app.schemas import userSchemas
from app.validators import userValidators

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=userSchemas.UserDisplay, dependencies=[Depends(userValidators.user_already_exists)],
             description="Endpoint for creating user")
def create_user(data: userSchemas.UserCreate, db: Session = Depends(get_db)):
    user = User(**data.dict(), id=str(uuid.uuid4()), password=get_password_hash(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("", response_model=userSchemas.UserDisplay, description="Endpoint to get current user")
def get_user(user: userSchemas.UserDisplay = Depends(get_current_active_user)):
    return user
