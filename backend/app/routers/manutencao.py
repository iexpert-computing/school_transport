# routers/manutencao.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.manutencao import create_manutencao, get_manutencao, get_manutencoes, update_manutencao, delete_manutencao
from backend.app.schemas.manutencao import ManutencaoCreate, ManutencaoOut
from backend.app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=ManutencaoOut)
def create_new_manutencao(manutencao: ManutencaoCreate, db: Session = Depends(get_db)):
    return create_manutencao(db, manutencao)

@router.get("/{manutencao_id}", response_model=ManutencaoOut)
def read_manutencao(manutencao_id: int, db: Session = Depends(get_db)):
    db_manutencao = get_manutencao(db, manutencao_id)
    if db_manutencao is None:
        raise HTTPException(status_code=404, detail="Manutenção não encontrada")
    return db_manutencao

@router.get("/", response_model=List[ManutencaoOut])
def read_manutencoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_manutencoes(db, skip=skip, limit=limit)

@router.put("/{manutencao_id}", response_model=ManutencaoOut)
def update_existing_manutencao(manutencao_id: int, manutencao: ManutencaoCreate, db: Session = Depends(get_db)):
    updated_manutencao = update_manutencao(db, manutencao_id, manutencao)
    if updated_manutencao is None:
        raise HTTPException(status_code=404, detail="Manutenção não encontrada")
    return updated_manutencao

@router.delete("/{manutencao_id}", response_model=ManutencaoOut)
def delete_existing_manutencao(manutencao_id: int, db: Session = Depends(get_db)):
    deleted_manutencao = delete_manutencao(db, manutencao_id)
    if deleted_manutencao is None:
        raise HTTPException(status_code=404, detail="Manutenção não encontrada")
    return deleted_manutencao
