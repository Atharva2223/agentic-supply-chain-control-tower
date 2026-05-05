from pydantic import BaseModel
from datetime import datetime


class ShipmentResponse(BaseModel):
    id: int
    shipment_id: str
    origin: str
    destination: str
    carrier: str
    status: str
    eta_hours: float
    delay_risk_score: float
    is_delayed: bool
    created_at: datetime

    class Config:
        from_attributes = True


class InventoryResponse(BaseModel):
    id: int
    sku: str
    warehouse: str
    quantity_on_hand: int
    reorder_point: int
    demand_forecast: int

    class Config:
        from_attributes = True


class SupplierResponse(BaseModel):
    id: int
    supplier_id: str
    name: str
    country: str
    risk_score: float
    on_time_delivery_rate: float

    class Config:
        from_attributes = True