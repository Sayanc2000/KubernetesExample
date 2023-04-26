import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Blog
from app.oauth2 import get_current_active_user
from app.schemas import userSchemas, blogSchemas

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.post("", response_model=blogSchemas.BlogDisplay, description="Endpoint to create blog")
def create_blog(data: blogSchemas.BlogCreate, user: userSchemas.UserDisplay = Depends(get_current_active_user),
                db: Session = Depends(get_db)):
    blog = Blog(**data.dict(), id=str(uuid.uuid4()), writerId=user.id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


@router.get("", response_model=List[blogSchemas.BlogDisplay])
def get_blogs(user: userSchemas.UserDisplay = Depends(get_current_active_user),
              db: Session = Depends(get_db)):
    blogs = db.query(Blog).where(Blog.writerId == user.id).all()
    return blogs
