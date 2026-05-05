import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT_DIR / "backend"
sys.path.append(str(BACKEND_DIR))

from app.database import SessionLocal, Base, engine
from app.models import Shipment, Inventory, Supplier


def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        db.query(Shipment).delete()
        db.query(Inventory).delete()
        db.query(Supplier).delete()

        shipments = [
            Shipment(
                shipment_id="SHP-1001",
                origin="Los Angeles",
                destination="Dallas",
                carrier="FedEx",
                status="in_transit",
                eta_hours=18,
                delay_risk_score=0.25,
                is_delayed=False,
            ),
            Shipment(
                shipment_id="SHP-1002",
                origin="Seattle",
                destination="Chicago",
                carrier="UPS",
                status="delayed",
                eta_hours=54,
                delay_risk_score=0.86,
                is_delayed=True,
            ),
            Shipment(
                shipment_id="SHP-1003",
                origin="New York",
                destination="Atlanta",
                carrier="DHL",
                status="in_transit",
                eta_hours=30,
                delay_risk_score=0.44,
                is_delayed=False,
            ),
            Shipment(
                shipment_id="SHP-1004",
                origin="San Francisco",
                destination="Phoenix",
                carrier="Maersk",
                status="delayed",
                eta_hours=72,
                delay_risk_score=0.91,
                is_delayed=True,
            ),
        ]

        inventory = [
            Inventory(
                sku="SKU-LAPTOP-001",
                warehouse="LA-WH-01",
                quantity_on_hand=120,
                reorder_point=50,
                demand_forecast=80,
            ),
            Inventory(
                sku="SKU-MONITOR-002",
                warehouse="DAL-WH-02",
                quantity_on_hand=20,
                reorder_point=40,
                demand_forecast=75,
            ),
            Inventory(
                sku="SKU-KEYBOARD-003",
                warehouse="CHI-WH-03",
                quantity_on_hand=15,
                reorder_point=25,
                demand_forecast=60,
            ),
        ]

        suppliers = [
            Supplier(
                supplier_id="SUP-001",
                name="Pacific Components Ltd",
                country="USA",
                risk_score=0.22,
                on_time_delivery_rate=0.96,
            ),
            Supplier(
                supplier_id="SUP-002",
                name="Global Micro Parts",
                country="Taiwan",
                risk_score=0.78,
                on_time_delivery_rate=0.81,
            ),
            Supplier(
                supplier_id="SUP-003",
                name="NorthStar Logistics",
                country="Mexico",
                risk_score=0.64,
                on_time_delivery_rate=0.88,
            ),
        ]

        db.add_all(shipments)
        db.add_all(inventory)
        db.add_all(suppliers)
        db.commit()

        print("Seed data inserted successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()