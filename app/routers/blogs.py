import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Blog
from app.oauth2 import get_current_active_user
from app.schemas import userSchemas, blogSchemas
from app.validators import blogValidators

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.post("", response_model=blogSchemas.BlogDisplay, description="Endpoint to create blog")
def create_blog(data: blogSchemas.BlogCreate, user: userSchemas.UserDisplay = Depends(get_current_active_user),
                db: Session = Depends(get_db)):
    blog = Blog(**data.dict(), id=str(uuid.uuid4()), writerId=user.id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


@router.get("", response_model=List[blogSchemas.BlogDisplay], description="Endpoint to get blogs by a user")
def get_blogs(user: userSchemas.UserDisplay = Depends(get_current_active_user),
              db: Session = Depends(get_db)):
    blogs = db.query(Blog).where(Blog.writerId == user.id).all()
    return blogs


@router.patch("/{blog_id}", response_model=blogSchemas.BlogDisplay, description="Endpoint to edit a blog")
def patch_blog(blog_id: str, data: blogSchemas.BlogPatch = Depends(),
               user: userSchemas.UserDisplay = Depends(get_current_active_user),
               db: Session = Depends(get_db), blog: Blog = Depends(blogValidators.blog_exists)):
    excluded_dict = data.dict(exclude_none=True)
    print(excluded_dict)
    for attr, value in excluded_dict.items():
        setattr(blog, attr, value)
    db.commit()
    db.refresh(blog)
    return blog
