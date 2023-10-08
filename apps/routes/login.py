from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List


login_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@login_router.get("/")
def read_root():
    return {"Hello": "World!!!!!"}