from pydantic import BaseModel, EmailStr
from enum import Enum

class NivelAcessoEnum(str, Enum):
    admin = "admin"
    gerente = "gerente"
    operador = "operador"

class GestorCreate(BaseModel):
    nome: str
    email: EmailStr
    senha_hash: str
    nivel_acesso: NivelAcessoEnum
    status_ativo: bool = True

class GestorOut(BaseModel):
    id_gestor: int
    nome: str
    email: EmailStr
    nivel_acesso: NivelAcessoEnum
    status_ativo: bool

    class Config:
        from_attributes = True
