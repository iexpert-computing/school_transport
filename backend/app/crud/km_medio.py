import requests
import numpy as np

# Sua chave da API do Mapbox
MAPBOX_API_KEY = "pk.eyJ1IjoiZWxvaWxzb25kb3NhbmpvcyIsImEiOiJjbHA4ajl5NzMwZXlvMmlqemNhZW84aTR0In0.xENAgw6IFeodsjlMFK8csw"

# Ponto fixo (origem) e lista de pontos ao redor (destinos)
fixed_point = (-23.55052, -46.633308)  # Exemplo: São Paulo, Brasil
surrounding_points = [
    (-23.56168, -46.62529),  # Exemplo 1
    (-23.54747, -46.63611),  # Exemplo 2
    (-23.56272, -46.65095),  # Exemplo 3
]

# URL base da API Directions do Mapbox
base_url = "https://api.mapbox.com/directions/v5/mapbox/driving"


def calculate_distances(fixed_point, surrounding_points, api_key):
    distances = []
    for point in surrounding_points:
        # Construindo a URL da requisição
        coordinates = f"{fixed_point[1]},{fixed_point[0]};{point[1]},{point[0]}"
        url = f"{base_url}/{coordinates}?access_token={api_key}&geometries=geojson"

        # Fazendo a requisição
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extrair distância em metros (rota mais curta)
            distance = data["routes"][0]["distance"]
            distances.append(distance / 1000)  # Convertendo para km
        else:
            print(f"Erro ao acessar o ponto {point}: {response.status_code}")

    return distances


# Calculando distâncias
distances = calculate_distances(fixed_point, surrounding_points, MAPBOX_API_KEY)

# Calculando a distância média
if distances:
    avg_distance = np.mean(distances)
    print(f"Distâncias (km): {distances}")
    print(f"Distância média (km): {avg_distance:.2f}")
else:
    print("Nenhuma distância foi calculada.")