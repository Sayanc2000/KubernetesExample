from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app import models
from app.database import engine
from app.middleware import add_process_time_header
from app.routers import users, auth, blogs, tasks
from app.schemas.basicSchemas import DefaultResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(tasks.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/", response_model=DefaultResponse, description="Root endpoint")
def root():
    return {
        "message": "Hello World"
    }


@app.get("/health", response_model=DefaultResponse, description="Health Endpoint")
def health():
    return {
        "message": "OK"
    }
