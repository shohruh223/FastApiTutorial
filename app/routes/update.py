from fastapi import APIRouter, Form, UploadFile, File, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.status import HTTP_302_FOUND
from ..database import SessionLocal
from ..models import User
import shutil, os
from fastapi.templating import Jinja2Templates

router = APIRouter()
UPLOAD_DIR = "app/static/uploads"
templates = Jinja2Templates(directory="app/templates")


@router.get("/update/{user_id}", response_class=HTMLResponse)
def update_form(request: Request, user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return templates.TemplateResponse("update.html", {"request": request, "user": user})


@router.post("/update/{user_id}")
async def update_user(user_id: int, name: str = Form(...), email: str = Form(...), image: UploadFile = File(None)):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.name = name
    user.email = email
    if image and image.filename:
        file_path = os.path.join(UPLOAD_DIR, image.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        user.image = image.filename
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=HTTP_302_FOUND)
