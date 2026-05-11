from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ExceptionTicket

router = APIRouter(prefix="/exceptions", tags=["Exceptions"])


@router.get("/")
def get_exceptions(db: Session = Depends(get_db)):
    return db.query(ExceptionTicket).all()