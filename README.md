# Finance Data Processing and Access Control Dashboard

This is the backend system for the Finance Dashboard, built using FastAPI, SQLite, and SQLAlchemy.

## Features
- **Role-based Access Control (RBAC):** Users can have `viewer`, `analyst`, or `admin` roles.
- **JWT Authentication:** Secure API endpoints via token-based auth.
- **Financial Records Management:** Complete CRUD operations for income and expense records.
- **Dashboard Summaries:** APIs for aggregate data like total income/expense, monthly trends, and category totals.

## Technology Stack
- **FastAPI**
- **SQLAlchemy** (ORM)
- **SQLite** (Database)
- **Pydantic** (Validation)
- **Passlib & Python-jose** (Security & JWT)

## Project Structure
- `app/core/`: Configuration and security logic.
- `app/database/`: Database orchestration.
- `app/models/`: SQLAlchemy database models.
- `app/schemas/`: Pydantic data schemas.
- `app/services/`: Core business logic for endpoints.
- `app/routes/`: FastAPI API routers.
- `app/main.py`: Application entrypoint.

## Setup Instructions

1. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

   The app will run by default at `http://localhost:8000`.

## API Endpoints Overview

- **Auth**
  - `POST /auth/token` - Get JWT token

- **Users (Admin Only)**
  - `GET /users/` - List users
  - `POST /users/` - Create a user
  - `PUT /users/{user_id}` - Update a user

- **Records (Analyst & Admin)**
  - `GET /records/` - List records (with filters like date range, category, type)
  - `POST /records/` - Create a new record
  - `PUT /records/{record_id}` - Update a record
  - `DELETE /records/{record_id}` - Soft-delete a record

- **Dashboard (Viewer, Analyst, Admin)**
  - `GET /dashboard/summary` - Net balance, total income/expense
  - `GET /dashboard/category-totals` - Aggregated totals per category
  - `GET /dashboard/monthly-trends` - Month-over-month income and expenses

## Seed Data
On the first startup, a default admin user is seeded into the database:
- **Username:** `admin`
- **Password:** `admin`

You can use these credentials in the Swagger UI (`http://localhost:8000/docs`) to authenticate and interact with the endpoints.

## Example Requests

**Login a user (cURL)**
```bash
curl -X 'POST' \
  'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin&password=admin'
```

**Get dashboard summary (Assuming token is saved in $TOKEN)**
```bash
curl -X 'GET' \
  'http://localhost:8000/dashboard/summary' \
  -H "Authorization: Bearer $TOKEN"
```
