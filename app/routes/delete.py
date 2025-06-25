from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND
from ..database import SessionLocal
from ..models import User

router = APIRouter()

@router.get("/delete/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=HTTP_302_FOUND)
