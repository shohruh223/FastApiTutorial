from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..database import SessionLocal
from ..models import User
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def read_users(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})
