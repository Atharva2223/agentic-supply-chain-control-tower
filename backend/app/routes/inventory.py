from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Inventory
from app.schemas import InventoryResponse

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/", response_model=list[InventoryResponse])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()


@router.get("/at-risk", response_model=list[InventoryResponse])
def get_at_risk_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).filter(
        Inventory.quantity_on_hand <= Inventory.reorder_point
    ).all()