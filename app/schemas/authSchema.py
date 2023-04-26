from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str


class UserToken(BaseModel):
    access_token: str
    token_type: str = "Bearer"
