from typing import List, Tuple

class Localizacao:
    """ Representa uma localização geográfica """
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def to_string(self) -> str:
        """ Converte a localização para string usada na API """
        return f"{self.longitude},{self.latitude}"

    @staticmethod
    def format_coordinates(localizacao: List["Localizacao"]) -> str:
        """ Formata uma lista de locais para string de coordenadas """
        return ";".join([loc.to_string() for loc in localizacao])