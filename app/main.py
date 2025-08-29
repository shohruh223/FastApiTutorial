from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
Base.metadata.create_all(bind=engine)


# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

# --------------------------------------------------


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request, "name": "Alijon"}
    return templates.TemplateResponse("index.html", context)


@app.get("/about", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request, "about": "Karatash neighbourhood"}
    return templates.TemplateResponse("about.html", context)
