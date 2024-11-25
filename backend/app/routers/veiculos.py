from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.veiculos import VeiculoCreate, VeiculoOut
from backend.app.crud.veiculos import get_veiculo, get_veiculos, create_veiculo, update_veiculo, delete_veiculo
from backend.app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=VeiculoOut)
def create_veiculo_route(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    return create_veiculo(db, veiculo)

@router.get("/{veiculo_id}", response_model=VeiculoOut)
def read_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    db_veiculo = get_veiculo(db, veiculo_id)
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return db_veiculo

@router.get("/", response_model=List[VeiculoOut])
def read_veiculos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_veiculos(db, skip=skip, limit=limit)

@router.put("/{veiculo_id}", response_model=VeiculoOut)
def update_veiculo_route(veiculo_id: int, veiculo_data: VeiculoCreate, db: Session = Depends(get_db)):
    db_veiculo = update_veiculo(db, veiculo_id, veiculo_data)
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return db_veiculo

@router.delete("/{veiculo_id}", response_model=VeiculoOut)
def delete_veiculo_route(veiculo_id: int, db: Session = Depends(get_db)):
    db_veiculo = delete_veiculo(db, veiculo_id)
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return db_veiculo
