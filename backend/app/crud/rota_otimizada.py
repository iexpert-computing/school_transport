import requests
from backend.app.config import MAPBOX_API_KEY, BASE_URL
from backend.app.models.localizacao import Localizacao
from typing import List

def get_best_route(origin: Localizacao, destinations: List[Localizacao]):
    """ Obtém a melhor rota usando o Mapbox """

    all_points = [origin] + destinations
    coordinates = Localizacao.format_coordinates(all_points)

    url = f"{BASE_URL}/{coordinates}?access_token={MAPBOX_API_KEY}&geometries=geojson&roundtrip=true&source=first"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "distance_km": data["trips"][0]["distance"] / 1000,
            "duration_min": data["trips"][0]["duration"] / 60,
            "geometry": data["trips"][0]["geometry"]
        }
    else:
        return {"error": "Erro ao acessar a API"}, 500