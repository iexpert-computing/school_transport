from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime

class RotaBase(BaseModel):
    nome_rota: str
    distancia_total: Optional[float] = None
    duracao_prevista: Optional[time] = None
    id_condutor: Optional[int] = None
    id_veiculo: Optional[int] = None
    status_rota: Optional[str] = "ativa"

class RotaCreate(RotaBase):
    pass

class RotaUpdate(RotaBase):
    pass

class RotaOut(RotaBase):
    id_rota: int

    class Config:
        from_attributes = True
