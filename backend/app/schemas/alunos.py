from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class AlunoBase(BaseModel):
    nome: str
    data_nascimento: date
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    id_ponto_embarque: Optional[int] = None
    necessidade_especial: bool = False
    status_ativo: bool = True

class AlunoCreate(AlunoBase):
    pass

class AlunoOut(AlunoBase):
    id_aluno: int

    class Config:
        from_attributes = True  # Atualização para Pydantic v2
