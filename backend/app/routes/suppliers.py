from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Supplier
from app.schemas import SupplierResponse

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.get("/", response_model=list[SupplierResponse])
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()


@router.get("/high-risk", response_model=list[SupplierResponse])
def get_high_risk_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).filter(Supplier.risk_score >= 0.7).all()