from pydantic import BaseModel
from datetime import date
from typing import Optional

class ContratoBase(BaseModel):
    numero_contrato: str
    data_inicio: date
    data_fim: date
    valor: float
    id_empresa: Optional[int]

class ContratoCreate(ContratoBase):
    pass

class ContratoUpdate(ContratoBase):
    pass

class ContratoOut(ContratoBase):
    id_contrato: int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2
