from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.rotas import RotaCreate, RotaOut, RotaUpdate
from backend.app.crud.rotas import create_rota, get_rota, get_rotas, update_rota, delete_rota
from backend.app.database import get_db
from typing import List


router = APIRouter()

@router.post("/", response_model=RotaOut)
def create_new_rota(rota: RotaCreate, db: Session = Depends(get_db)):
    return create_rota(db, rota)

@router.get("/{rota_id}", response_model=RotaOut)
def read_rota(rota_id: int, db: Session = Depends(get_db)):
    db_rota = get_rota(db, rota_id)
    if db_rota is None:
        raise HTTPException(status_code=404, detail="Rota not found")
    return db_rota

@router.get("/", response_model=List[RotaOut])
def read_rotas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_rotas(db, skip=skip, limit=limit)

@router.put("/{rota_id}", response_model=RotaOut)
def update_existing_rota(rota_id: int, rota: RotaUpdate, db: Session = Depends(get_db)):
    updated_rota = update_rota(db, rota_id, rota)
    if updated_rota is None:
        raise HTTPException(status_code=404, detail="Rota not found")
    return updated_rota

@router.delete("/{rota_id}", response_model=RotaOut)
def delete_existing_rota(rota_id: int, db: Session = Depends(get_db)):
    deleted_rota = delete_rota(db, rota_id)
    if deleted_rota is None:
        raise HTTPException(status_code=404, detail="Rota not found")
    return deleted_rota