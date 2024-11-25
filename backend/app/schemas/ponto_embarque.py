# backend/app/schemas/ponto_embarque.py

from pydantic import BaseModel

class PontoEmbarqueBase(BaseModel):
    endereco_ponto: str
    latitude: float
    longitude: float

class PontoEmbarqueCreate(PontoEmbarqueBase):
    pass

class PontoEmbarqueUpdate(PontoEmbarqueBase):
    pass

class PontoEmbarqueOut(PontoEmbarqueBase):
    id_ponto: int

    class Config:
        from_attributes = True
