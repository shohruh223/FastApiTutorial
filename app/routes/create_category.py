import os
import shutil
from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND
from ..database import SessionLocal
from ..models import Category
from fastapi.templating import Jinja2Templates

router = APIRouter()
UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
templates = Jinja2Templates(directory="app/templates")


@router.get("/create-category", response_class=HTMLResponse)
def create_form(request: Request):
    return templates.TemplateResponse("create_category.html", {"request": request})


@router.post("/create-category")
async def create_category(request: Request):
    form = await request.form()
    title = form.get("title")

    db = SessionLocal()
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.close()

    return RedirectResponse("/", status_code=HTTP_302_FOUND)


