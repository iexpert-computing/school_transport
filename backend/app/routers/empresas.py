from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.empresas import EmpresaCreate, EmpresaOut
from backend.app.crud.empresas import get_empresa, get_empresas, create_empresa, update_empresa, delete_empresa
from backend.app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=EmpresaOut)
def create_empresa_route(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    return create_empresa(db, empresa)

@router.get("/{empresa_id}", response_model=EmpresaOut)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = get_empresa(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@router.get("/", response_model=List[EmpresaOut])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_empresas(db, skip=skip, limit=limit)

@router.put("/{empresa_id}", response_model=EmpresaOut)
def update_empresa_route(empresa_id: int, empresa_data: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = update_empresa(db, empresa_id, empresa_data)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@router.delete("/{empresa_id}", response_model=EmpresaOut)
def delete_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = delete_empresa(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa
