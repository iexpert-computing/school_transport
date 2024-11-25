# backend/app/routers/ponto_embarque.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.ponto_embarque import (
    create_ponto_embarque,
    get_pontos_embarque,
    get_ponto_embarque,
    update_ponto_embarque,
    delete_ponto_embarque
)
from backend.app.schemas.ponto_embarque import PontoEmbarqueCreate, PontoEmbarqueUpdate, PontoEmbarqueOut
from backend.app.database import get_db

router = APIRouter()

# CREATE
@router.post("/", response_model=PontoEmbarqueOut)
def create_ponto_embarque_route(ponto_embarque: PontoEmbarqueCreate, db: Session = Depends(get_db)):
    return create_ponto_embarque(db, ponto_embarque)

# READ ALL
@router.get("/", response_model=List[PontoEmbarqueOut])
def read_pontos_embarque(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_pontos_embarque(db, skip=skip, limit=limit)

# READ BY ID
@router.get("/{ponto_id}", response_model=PontoEmbarqueOut)
def read_ponto_embarque(ponto_id: int, db: Session = Depends(get_db)):
    db_ponto = get_ponto_embarque(db, ponto_id)
    if db_ponto is None:
        raise HTTPException(status_code=404, detail="Ponto de embarque não encontrado")
    return db_ponto

# UPDATE
@router.put("/{ponto_id}", response_model=PontoEmbarqueOut)
def update_ponto_embarque_route(ponto_id: int, ponto_embarque: PontoEmbarqueUpdate, db: Session = Depends(get_db)):
    db_ponto = update_ponto_embarque(db, ponto_id, ponto_embarque)
    if db_ponto is None:
        raise HTTPException(status_code=404, detail="Ponto de embarque não encontrado")
    return db_ponto

# DELETE
@router.delete("/{ponto_id}", response_model=PontoEmbarqueOut)
def delete_ponto_embarque_route(ponto_id: int, db: Session = Depends(get_db)):
    db_ponto = delete_ponto_embarque(db, ponto_id)
    if db_ponto is None:
        raise HTTPException(status_code=404, detail="Ponto de embarque não encontrado")
    return db_ponto
