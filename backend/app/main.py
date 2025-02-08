from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple
from backend.app.routers import rota_otimizada  # Importe o roteador

app = FastAPI()

app.include_router(rota_otimizada.router)  # Inclua o roteador

class RouteRequest(BaseModel):
    origin: Tuple[float, float]
    destinations: List[Tuple[float, float]]

@app.post("/rota")  # ✅ Confirme que está aceitando POST
def calculate_route(request: RouteRequest):
    return {"message": "Rota processada com sucesso"}
