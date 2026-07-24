# Expert Decision Replay Platform — Backend Setup

## 1. Copy files into your project
Unzip `edrp_backend.zip` and copy the contents of `backend/` into the
`backend/` folder you already created.

## 2. Install dependencies (matches your mentor's commands)
```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install psycopg2-binary
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
pip install bcrypt==4.0.1
pip install python-multipart
pip install "pydantic[email]"
```
Or just: `pip install -r requirements.txt`

**Important:** pin `bcrypt==4.0.1` — newer bcrypt versions break passlib's hashing
and password login will silently fail with an internal server error.

## 3. Database
By default this connects to PostgreSQL:
```
postgresql://edrp_user:edrp_pass@localhost:5432/edrp_db
```
Create that database/user in Postgres first, or set your own via the
`DATABASE_URL` environment variable.

**For quick local testing without installing Postgres**, you can temporarily run:
```
set DATABASE_URL=sqlite:///./edrp.db        (Windows)
export DATABASE_URL=sqlite:///./edrp.db     (Mac/Linux)
```
Tables auto-create on first run — no manual migration needed for now.

## 4. Run the server
```
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs for interactive Swagger UI — this is the
easiest way to test every endpoint without building the frontend yet.

## 5. Roles
Roles (`employee`, `reviewer`, `manager`, `admin`) are auto-created the first
time someone registers with that role name — you don't need to seed them
manually.

## Quick test flow (via /docs or curl)
1. `POST /api/auth/register` — create an admin user
2. `POST /api/auth/login` — get a JWT token (use the "Authorize" button in /docs)
3. `POST /api/decision-categories` — create a category
4. `POST /api/decisions` — create a decision
5. `POST /api/decisions/{id}/alternatives` — add an alternative
6. `POST /api/decisions/{id}/approvals` — assign an approver
7. `PUT /api/decisions/approvals/{id}/decide` — approve/reject (logged into that approver's account)

## What's implemented (all 13 tables from your mentor's list)
Users, Roles, Teams, Decisions, Decision Categories, Alternatives,
Risk Assessments, Comments, Discussion Threads, Approvals, Notifications,
Documents, Audit Logs.

## Not yet wired to a router (models + schemas exist, endpoints coming next)
- Notifications (auto-creation on approval events)
- Documents (file upload endpoint)
- Audit log viewer endpoint (entries are already being written automatically
  when decisions are created/updated/approved)

Ask me to build these next, or to start on the React frontend.
