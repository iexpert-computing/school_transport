from pydantic import BaseModel
from typing import List


class RouteRequest(BaseModel):
    origin: List[float]  # [latitude, longitude]
    destinations: List[List[float]]  # Lista de pontos [lat, lon]


class RouteResponse(BaseModel):
    distance_km: float
    duration_min: float
    geometry: dict
