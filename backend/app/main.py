from fastapi import FastAPI
from app.database import Base, engine
from app.routes import shipments, inventory, suppliers,detection
from app.routes import exceptions, decisions

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agentic Supply Chain Control Tower",
    version="0.2.0"
)

app.include_router(shipments.router)
app.include_router(inventory.router)
app.include_router(suppliers.router)
app.include_router(detection.router)
app.include_router(exceptions.router)
app.include_router(decisions.router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Agentic Supply Chain Control Tower",
        "version": "0.2.0"
    }