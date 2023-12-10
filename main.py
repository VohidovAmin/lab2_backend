from typing import Union
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from routers import users
import uvicorn

app = FastAPI()

app.include_router(users.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>This is the root</h1>"