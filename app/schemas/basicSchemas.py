from pydantic import BaseModel


class DefaultResponse(BaseModel):
    message: str

    class Config:
        orm_mode: True


class ErrorResponse(BaseModel):
    detail: str

    class Config:
        orm_mode: True
