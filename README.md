# Geek Advice Demo

A small control panel that shows how the backend connects with the visual parts.

- `main.py`: Python backend (FastAPI) with 4 endpoints
- `index.html`: the control panel that calls those endpoints

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 for the panel, or http://127.0.0.1:8000/docs to see the API.
