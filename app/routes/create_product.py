import os
import shutil
from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND
from ..database import SessionLocal
from ..models import Product
from fastapi.templating import Jinja2Templates

router = APIRouter()
UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
templates = Jinja2Templates(directory="app/templates")


@router.get("/create-product", response_class=HTMLResponse)
def create_form(request: Request):
    return templates.TemplateResponse("create_product.html", {"request": request})


@router.post("/create-product")
async def create_user(request: Request, image: UploadFile = File(...),):
    form = await request.form()

    title = form.get("title")
    category_id = int(form.get("category_id"))
    price = float(form.get("price"))
    review_raw = form.get("review")
    review = int(review_raw) if review_raw else None
    text = form.get("text")
    quantity = int(form.get("quantity"))

    file_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db = SessionLocal()
    product = Product(
        image=image.filename,
        title=title,
        category_id=category_id,
        price=price,
        review=review,
        text=text,
        quantity=quantity
    )
    db.add(product)
    db.commit()
    db.close()

    return RedirectResponse("/", status_code=HTTP_302_FOUND)

