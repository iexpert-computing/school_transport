from pydantic import BaseModel
from datetime import date
from typing import Optional

# Esquema para criar um novo condutor
class CondutorCreate(BaseModel):
    nome: str
    cnh: str
    validade_cnh: date
    telefone: Optional[str] = None
    id_veiculo: Optional[int] = None

# Esquema para atualizar informações do condutor
class CondutorUpdate(BaseModel):
    nome: Optional[str] = None
    cnh: Optional[str] = None
    validade_cnh: Optional[date] = None
    telefone: Optional[str] = None
    id_veiculo: Optional[int] = None
    status_ativo: Optional[bool] = None

# Esquema para resposta de dados do condutor
class CondutorResponse(BaseModel):
    id_condutor: int
    nome: str
    cnh: str
    validade_cnh: date
    telefone: Optional[str]
    id_veiculo: Optional[int]
    status_ativo: bool

    class Config:
        from_attributes = True
