from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

from app.security import short_ref, mask_secret
from app.config import get_settings

app = FastAPI(title="AppSec Demo")

class EchoIn(BaseModel):
    message: str

@app.get("/health")
def health():
    logging.info("health probe id=%s", short_ref("health"))
    return {"status": "ok", "service": get_settings().api_name}

@app.post("/echo")
def echo(payload: EchoIn):
    # Demostración de logging seguro: no imprimir secretos
    logging.info("echo req id=%s msg_len=%d", short_ref(payload.message), len(payload.message))
    if len(payload.message) > 2000:
        raise HTTPException(status_code=413, detail="message too large")
    return {"echo": payload.message}
