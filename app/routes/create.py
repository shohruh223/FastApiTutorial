import os
import shutil
from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND
from ..database import SessionLocal
from ..models import User
from fastapi.templating import Jinja2Templates

router = APIRouter()
UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
templates = Jinja2Templates(directory="app/templates")


@router.get("/create", response_class=HTMLResponse)
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@router.post("/create")
async def create_user(image: UploadFile = File(...), name: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db = SessionLocal()
    user = User(image=image.filename, name=name)
    db.add(user)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=HTTP_302_FOUND)
