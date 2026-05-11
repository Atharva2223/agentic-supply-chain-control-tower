from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.detection_service import (
    detect_shipment_issues,
    detect_inventory_issues,
    detect_supplier_risks,
)

router = APIRouter(prefix="/detect", tags=["Detection"])


@router.post("/run")
def run_detection(db: Session = Depends(get_db)):
    detect_shipment_issues(db)
    detect_inventory_issues(db)
    detect_supplier_risks(db)

    return {"message": "Detection completed"}