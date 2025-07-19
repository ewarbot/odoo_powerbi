from fastapi import FastAPI
from odoo_rpc import OdooConnector
from redis_cache import cache_get, cache_set
import json
from fastapi import Depends
from auth import get_current_user
from auth import create_token
from fastapi import Form

app = FastAPI()
odoo = OdooConnector()

@app.get("/")
def root():
    return {"message": "API FastAPI + Nginx + Redis conectada a Odoo"}

@app.get("/partners")
def get_partners(limit: int = 10, user: str = Depends(get_current_user)):
    cache_key = f"partners_{limit}"
    cached = cache_get(cache_key)
    if cached:
        return json.loads(cached)
    data = odoo.get_partners(limit)
    cache_set(cache_key, json.dumps(data))
    return data

@app.post("/token")
def generate_token(username: str = Form(...), password: str = Form(...)):
    # Esto es solo de prueba. Deberías validar contra una base real
    if username == "admin" and password == "admin123":
        token = create_token({"sub": username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
