from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import SessionLocal
from app.models import Product
from sqlalchemy.orm import Session

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @router.get("/shop", response_class=HTMLResponse)
# async def shop_func(request: Request):
#     db = SessionLocal()
#     products = db.query(Product).all()
#     db.close()
#     return templates.TemplateResponse("shop.html", {
#         "request": request,
#         "products": products
#     })


@router.get("/shop", response_class=HTMLResponse)
async def shop_func(request: Request, page: int = 1, db: Session = Depends(get_db)):
    per_page = 6
    products = db.query(Product).offset((page - 1) * per_page).limit(per_page).all()
    total = db.query(Product).count()
    total_pages = (total + per_page - 1) // per_page

    return templates.TemplateResponse("shop.html", {
        "request": request,
        "products": products,
        "page": page,
        "total_pages": total_pages
    })


@router.get("/shop/{product_id}", response_class=HTMLResponse)
async def shop_detail(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return templates.TemplateResponse("shop-detail.html", {
        "request": request,
        "product": product})

