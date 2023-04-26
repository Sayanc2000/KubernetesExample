from typing import Optional

from pydantic import BaseModel

from app.schemas.userSchemas import UserDisplay


class BlogCreate(BaseModel):
    name: str
    description: str


class BlogPatch(BaseModel):
    name: Optional[str]
    description: Optional[str]


class BlogDisplay(BlogCreate):
    id: str
    writer: UserDisplay

    class Config:
        orm_mode = True
