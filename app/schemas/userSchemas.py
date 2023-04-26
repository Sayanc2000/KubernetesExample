from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str


class UserDisplay(UserBase):
    id: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    def dict(self):
        return {
            "email": self.email,
            "name": self.name
        }
