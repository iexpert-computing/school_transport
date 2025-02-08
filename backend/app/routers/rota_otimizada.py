from fastapi import APIRouter
from backend.app.schemas.rota_otimizada import RouteRequest, RouteResponse
from backend.app.crud.rota_otimizada import get_best_route
from backend.app.models.localizacao import Localizacao

router = APIRouter()


@router.post("/rota", response_model=RouteResponse)
def calculate_route(request: RouteRequest):
    """ Endpoint para calcular a melhor rota """
    origin = Localizacao(request.origin[0], request.origin[1])
    destinations = [Localizacao(lat, lon) for lat, lon in request.destinations]

    result = get_best_route(origin, destinations)

    if "error" in result:
        return {"error": result["error"]}
    return RouteResponse(**result)
