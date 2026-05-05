from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from datetime import datetime
from app.database import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(String, unique=True, index=True)
    origin = Column(String)
    destination = Column(String)
    carrier = Column(String)
    status = Column(String)
    eta_hours = Column(Float)
    delay_risk_score = Column(Float)
    is_delayed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True)
    warehouse = Column(String)
    quantity_on_hand = Column(Integer)
    reorder_point = Column(Integer)
    demand_forecast = Column(Integer)


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(String, unique=True)
    name = Column(String)
    country = Column(String)
    risk_score = Column(Float)
    on_time_delivery_rate = Column(Float)


class ExceptionTicket(Base):
    __tablename__ = "exception_tickets"

    id = Column(Integer, primary_key=True, index=True)
    issue_type = Column(String)
    severity = Column(String)
    summary = Column(Text)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)


class AgentDecision(Base):
    __tablename__ = "agent_decisions"

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String)
    action_type = Column(String)
    reasoning = Column(Text)
    approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)