from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AgentDecision

router = APIRouter(prefix="/decisions", tags=["Decisions"])


@router.get("/")
def get_decisions(db: Session = Depends(get_db)):
    return db.query(AgentDecision).all()