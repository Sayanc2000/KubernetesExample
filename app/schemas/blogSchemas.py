from pydantic import BaseModel

from app.schemas.userSchemas import UserDisplay


class BlogCreate(BaseModel):
    name: str
    description: str


class BlogDisplay(BlogCreate):
    id: str
    writer: UserDisplay

    class Config:
        orm_mode = True
