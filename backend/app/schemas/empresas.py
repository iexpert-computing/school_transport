from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class EmpresaBase(BaseModel):
    nome_empresa: str
    cnpj: str = Field(..., min_length=14, max_length=20)
    telefone: Optional[str] = None
    email_empresa: Optional[EmailStr] = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    id_empresa: int

    class Config:
        from_attributes = True  # Atualização para Pydantic v2
