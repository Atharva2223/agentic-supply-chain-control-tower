# 🏗️ Agentic Supply Chain Control Tower

> An AI-driven control tower that monitors supply chain operations, detects disruptions, and enables intelligent decision-making using agent-based workflows and MCP (Model Context Protocol).

---

## 📌 Project Status

**🟡 In Progress** — Transitioning from data layer → agentic intelligence layer

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1 — Infrastructure | ✅ Complete | PostgreSQL + Docker setup |
| Phase 2 — Data & APIs | ✅ Complete | Models, REST endpoints, risk filters |
| Phase 3 — MCP Server | 🔄 In Progress | Supply chain tooling via Python MCP SDK |
| Phase 4 — AI Agents | 🔜 Planned | LangGraph / OpenAI Agents SDK |
| Phase 5 — Frontend | 🔜 Planned | Real-time Next.js dashboard |

---

## 🧠 Overview

This project simulates a real-world **Supply Chain Control Tower** used by logistics and operations teams to:

- 📦 Track shipments in real-time
- 🏭 Monitor inventory levels across warehouses
- ⚠️ Detect delays and supply chain risks
- 🤝 Identify and score supplier issues
- 🤖 Enable AI agents to recommend or execute corrective actions

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER / CLIENT                         │
└──────────────────────────┬──────────────────────────────────┘
                           │  HTTP / WebSocket
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  NEXT.JS FRONTEND  (planned)                 │
│          Real-time Dashboard · Alerts · What-if UI          │
└──────────────────────────┬──────────────────────────────────┘
                           │  REST / JSON
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND  ✅                        │
│                                                             │
│   ┌──────────────┐  ┌────────────────┐  ┌───────────────┐  │
│   │  /shipments  │  │   /inventory   │  │   /suppliers  │  │
│   │  (+ delayed) │  │   (+ at-risk)  │  │  (+ hi-risk)  │  │
│   └──────────────┘  └────────────────┘  └───────────────┘  │
│                                                             │
│              Pydantic Validation · Risk Filters             │
└──────────────────────────┬──────────────────────────────────┘
                           │  ORM Queries
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                 SQLALCHEMY ORM  ✅                            │
│   Shipment · Inventory · Supplier · ExceptionTicket         │
│                     AgentDecision                           │
└──────────────────────────┬──────────────────────────────────┘
                           │  SQL
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               POSTGRESQL  (Docker)  ✅                       │
└─────────────────────────────────────────────────────────────┘

                    ─ ─ ─  AGENTIC LAYER  ─ ─ ─

┌─────────────────────────────────────────────────────────────┐
│                   MCP SERVER  (planned)                      │
│                                                             │
│   ┌───────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│   │  Shipment     │  │   Inventory     │  │  Supplier   │  │
│   │  Tool         │  │   Risk Tool     │  │  Score Tool │  │
│   └───────────────┘  └─────────────────┘  └─────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │  Tool Calls
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    AI AGENTS  (planned)                      │
│                                                             │
│   ┌──────────────────┐       ┌─────────────────────────┐   │
│   │  Delay Detection │       │  Inventory Risk Analyst  │   │
│   │  Agent           │       │  Agent                   │   │
│   └──────────────────┘       └─────────────────────────┘   │
│                                                             │
│   ┌──────────────────────────────────────────────────────┐  │
│   │           Supplier Risk Scoring Agent                │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                             │
│         LangGraph / OpenAI Agents SDK · Decision Log        │
└─────────────────────────────────────────────────────────────┘

              ─ ─ ─  OBSERVABILITY (planned)  ─ ─ ─

┌───────────────────────┐      ┌───────────────────────────┐
│   KAFKA  Event Stream │      │  OpenTelemetry + Grafana  │
│   (planned)           │      │  (planned)                │
└───────────────────────┘      └───────────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend API | FastAPI |
| Database | PostgreSQL (Docker) |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Agent Framework | LangGraph / OpenAI Agents SDK *(planned)* |
| MCP Server | Python MCP SDK *(planned)* |
| Frontend | Next.js *(planned)* |
| Streaming | Kafka *(planned)* |
| Observability | OpenTelemetry + Grafana *(planned)* |

---

## 📦 Features

### ✅ Phase 1–2 (Completed)

- PostgreSQL database setup with Docker Compose
- Data models for:
  - `Shipments` — tracking, status, ETA, carrier
  - `Inventory` — warehouse stock levels, SKUs
  - `Suppliers` — risk score, lead time, reliability
  - `ExceptionTickets` — triggered alerts and issues
  - `AgentDecisions` — logged AI recommendations
- REST APIs for shipments, inventory, and suppliers
- Risk-based filtering: delayed shipments, at-risk inventory, high-risk suppliers
- Synthetic data generator for local development and testing

---

## 🔌 API Endpoints

### Shipments
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/shipments/` | All shipments |
| `GET` | `/shipments/delayed` | Filtered: delayed shipments |
| `GET` | `/shipments/{id}` | Single shipment detail |

### Inventory
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/inventory/` | All inventory records |
| `GET` | `/inventory/at-risk` | Filtered: low-stock items |

### Suppliers
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/suppliers/` | All suppliers |
| `GET` | `/suppliers/high-risk` | Filtered: risky suppliers |

---

## 🧪 Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/agentic-supply-chain-control-tower.git
cd agentic-supply-chain-control-tower
```

### 2. Start the database
```bash
docker compose -f infra/docker-compose.yml up -d
```

### 3. Start the backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### 4. Seed sample data
```bash
cd ..
python -m data.seed_data
```

### 5. Explore the API
Open **http://127.0.0.1:8000/docs** in your browser for the interactive Swagger UI.

---

## 📊 Example Use Case

```
1. A shipment misses its ETA window
         │
         ▼
2. API flags it as high-risk (GET /shipments/delayed)
         │
         ▼
3. Inventory impact is evaluated (GET /inventory/at-risk)
         │
         ▼
4. AI agent recommends rerouting or expedited sourcing
         │
         ▼
5. Decision is logged to AgentDecisions table
         │
         ▼
6. Operations team reviews and approves action
```

---

## 🔮 Upcoming Features

- **MCP Server** — expose supply chain tools via Python MCP SDK
- **AI Agents** for:
  - Shipment delay detection and rerouting
  - Inventory risk analysis and reorder recommendations
  - Supplier risk scoring and alternative sourcing
- **What-if Simulation Engine** — model disruption scenarios
- **Real-time Dashboard** — Next.js with live alerts
- **Kafka Event Streaming** — event-driven architecture
- **Observability** — OpenTelemetry traces + Grafana dashboards

---

## 🧠 Learning Outcomes

- Backend system design for operations-critical software
- Relational database modeling for supply chain domains
- REST API development with FastAPI and SQLAlchemy
- Docker-based local infrastructure
- Foundations of agentic AI systems with tool use and MCP

---

## 👨‍💻 Author

**Atharva Patade**
MS Information Systems, CSULB
Aspiring AI/ML Engineer

---

*Built to explore the intersection of supply chain operations and agentic AI — from data layer to autonomous decision-making.*
