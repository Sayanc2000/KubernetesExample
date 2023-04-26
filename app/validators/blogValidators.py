from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Blog


def blog_exists(request: Request, db: Session = Depends(get_db)) -> Blog or None:
    blog_id = None
    for key, val in request.path_params.items():
        if key == "blog_id":
            blog_id = val
    if not blog_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="blog_id not found")

    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dataset does not exist")
