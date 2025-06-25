from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine
from .routes import create, read

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
Base.metadata.create_all(bind=engine)
app.include_router(read.router)
app.include_router(create.router)


# @app.get("/", response_class=HTMLResponse)
# def home(request: Request):
#     context = {"request": request, "name": "Alijon"}
#     return templates.TemplateResponse("index.html", context)
