from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User


async def user_already_exists(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    email = data["email"]
    user = db.query(User).where(User.email == email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
