from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Shipment
from app.schemas import ShipmentResponse

router = APIRouter(prefix="/shipments", tags=["Shipments"])


@router.get("/", response_model=list[ShipmentResponse])
def get_shipments(db: Session = Depends(get_db)):
    return db.query(Shipment).all()


@router.get("/delayed", response_model=list[ShipmentResponse])
def get_delayed_shipments(db: Session = Depends(get_db)):
    return db.query(Shipment).filter(Shipment.is_delayed == True).all()


@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment_by_id(shipment_id: str, db: Session = Depends(get_db)):
    return db.query(Shipment).filter(Shipment.shipment_id == shipment_id).first()