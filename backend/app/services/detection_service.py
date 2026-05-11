from sqlalchemy.orm import Session
from app.models import Shipment, Inventory, Supplier, ExceptionTicket, AgentDecision


def detect_shipment_issues(db: Session):
    delayed_shipments = db.query(Shipment).filter(Shipment.is_delayed == True).all()

    for shipment in delayed_shipments:
        summary = f"Shipment {shipment.shipment_id} is delayed with risk score {shipment.delay_risk_score}"

        ticket = ExceptionTicket(
            issue_type="shipment_delay",
            severity="high" if shipment.delay_risk_score > 0.8 else "medium",
            summary=summary,
        )

        decision = AgentDecision(
            agent_name="DelayDetectionAgent",
            action_type="flag_delay",
            reasoning=f"Delay risk score is {shipment.delay_risk_score}, above threshold",
        )

        db.add(ticket)
        db.add(decision)

    db.commit()


def detect_inventory_issues(db: Session):
    risky_inventory = db.query(Inventory).filter(
        Inventory.quantity_on_hand <= Inventory.reorder_point
    ).all()

    for item in risky_inventory:
        summary = f"Inventory risk for SKU {item.sku} at {item.warehouse}"

        ticket = ExceptionTicket(
            issue_type="inventory_risk",
            severity="high",
            summary=summary,
        )

        decision = AgentDecision(
            agent_name="InventoryAgent",
            action_type="flag_inventory_risk",
            reasoning="Stock below reorder point",
        )

        db.add(ticket)
        db.add(decision)

    db.commit()


def detect_supplier_risks(db: Session):
    risky_suppliers = db.query(Supplier).filter(Supplier.risk_score >= 0.7).all()

    for supplier in risky_suppliers:
        summary = f"Supplier {supplier.name} has high risk score {supplier.risk_score}"

        ticket = ExceptionTicket(
            issue_type="supplier_risk",
            severity="high",
            summary=summary,
        )

        decision = AgentDecision(
            agent_name="SupplierRiskAgent",
            action_type="flag_supplier_risk",
            reasoning="Risk score exceeds threshold",
        )

        db.add(ticket)
        db.add(decision)

    db.commit()