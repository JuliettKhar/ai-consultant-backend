# 🧠 AI Consultant Backend

FastAPI project providing the backend API for the AI Consultant application. Supports chat sessions, admin tools, and PostgreSQL integration.

---

## 📦 Tech Stack

- 🔧 **FastAPI** – for RESTful APIs
- 🧬 **SQLAlchemy** + **Alembic** – ORM & migrations
- 🐘 **PostgreSQL** – database
- 🐳 **Docker** / **Docker Compose** – containerization

---

## 🚀 Quick Start (local, no Docker)

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-consultant-backend.git
cd ai-consultant-backend
```

2. Adjust the .env file:
```bash
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=appdb
POSTGRES_PORT=5432

# Backend
DB_HOST=db
DB_PORT=5432
DB_NAME=appdb
DB_USER=postgres
DB_PASSWORD=postgres
```
2.Start services:
```bash
  docker compose up --build
```
3.Access API docs: http://localhost:8000/docs

📁 Project Structure
```bash
.
├── app/
│   ├── main.py            # Entry point
│   ├── models/            # SQLAlchemy models
│   ├── routers/           # API routers
│   ├── services/          # Business logic
│   └── database.py        # DB connection setup
├── alembic/               # Database migrations
├── .env                   # Environment variables
├── Dockerfile
├── docker-compose.yml
└── README.md
```

🗃️ Migrations
1. Create migration:
```bash
  alembic revision --autogenerate -m "your message"
```
2.Apply migration:
```bash
  alembic upgrade head
```
