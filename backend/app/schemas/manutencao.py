# schemas/manutencao.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class ManutencaoBase(BaseModel):
    id_veiculo: int
    data_manutencao: date
    tipo_manutencao: str
    descricao: Optional[str] = None
    custo: Optional[float] = None

class ManutencaoCreate(ManutencaoBase):
    pass

class ManutencaoOut(ManutencaoBase):
    id_manutencao: int

    class Config:
        from_attributes = True
