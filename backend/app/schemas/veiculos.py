from pydantic import BaseModel, Field
from typing import Optional, Literal

class VeiculoBase(BaseModel):
    modelo: str
    placa: str = Field(..., min_length=7, max_length=10)
    ano: int
    capacidade: int
    status_veiculo: Optional[Literal['ativo', 'inativo', 'manutencao']] = 'ativo'
    id_empresa: Optional[int] = None

class VeiculoCreate(VeiculoBase):
    pass

class VeiculoOut(VeiculoBase):
    id_veiculo: int

    class Config:
        from_attributes = True  # Para Pydantic v2
