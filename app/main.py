from typing import Union
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
import uvicorn

from app.routers import users, drivers, trips
from app.config import POSTGRES_DATABASE_URL
from app.database import db_manager

db_manager.init(POSTGRES_DATABASE_URL)

app = FastAPI()

app.include_router(users.router)
app.include_router(drivers.router)
app.include_router(trips.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>This is the root</h1>"