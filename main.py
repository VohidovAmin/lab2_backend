from typing import Union
from fastapi import FastAPI
from routers import users
import uvicorn

app = FastAPI()

app.include_router(users.router)