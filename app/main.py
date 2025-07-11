from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine
from .routes import create_product, create_category, shop

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
Base.metadata.create_all(bind=engine)

app.include_router(create_category.router)
app.include_router(create_product.router)
app.include_router(shop.router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/testimonial", response_class=HTMLResponse)
async def testimonial(request: Request):
    return templates.TemplateResponse("testimonial.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/checkout", response_class=HTMLResponse)
async def checkout(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})


@app.get("/cart", response_class=HTMLResponse)
async def cart(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})


@app.get("/404", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})


# register
@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})
