from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Geek Advice Demo")

BASE_DIR = Path(__file__).parent


# The visual part: serves the control panel page
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


# Endpoint 1: general system status
@app.get("/api/status")
def get_status():
    return {"server": "online", "version": "1.0", "uptime": "99.9%"}


# Endpoint 2: recent users
@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Ana Torres", "role": "Admin"},
        {"id": 2, "name": "Luis Rojas", "role": "Editor"},
        {"id": 3, "name": "Maria Quispe", "role": "Viewer"},
    ]


# Endpoint 3: daily metrics
@app.get("/api/metrics")
def get_metrics():
    return {"visits_today": 1250, "new_users": 38, "orders": 74}


# Endpoint 4: system alerts
@app.get("/api/alerts")
def get_alerts():
    return [
        {"level": "info", "message": "Backup completed successfully"},
        {"level": "warning", "message": "Disk usage at 82%"},
    ]
