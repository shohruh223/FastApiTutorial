from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routes import create, read, update, delete

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

Base.metadata.create_all(bind=engine)
app.include_router(read.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)

