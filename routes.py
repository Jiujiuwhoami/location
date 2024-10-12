# routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")
GO_URL = os.getenv('GO_URL', '/static/js/coffee.html')  # 定位成功后需要跳转的 url
ERROR_URL = os.getenv('ERROR_URL', '/static/js/coffee2.html')  # 定位失败后需要跳转的 url

@router.get("/location", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "go_url": GO_URL, "error_url": ERROR_URL})

