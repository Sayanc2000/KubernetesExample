from typing import Union

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


class User(BaseModel):
    id: Union[str, None] = None
    email: Union[str, None] = None
    name: Union[str, None] = None


class UserInDB(User):
    hashed_password: str
