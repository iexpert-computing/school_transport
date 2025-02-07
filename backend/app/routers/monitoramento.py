from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app import crud
from backend.app.schemas.monitoramento import MonitoramentoCreate, MonitoramentoUpdate, MonitoramentoOut
from backend.app.database import get_db

router = APIRouter(
    prefix="/monitoramento",
    tags=["monitoramento"],
)

# Criar novo monitoramento
@router.post("/", response_model=MonitoramentoOut)

def create_monitoramento(monitoramento: MonitoramentoCreate, db: Session = Depends(get_db)):
    return crud.create_monitoramento(db=db, monitoramento=monitoramento)

# Buscar monitoramento por id
@router.get("/{id_monitoramento}", response_model=MonitoramentoOut)

def read_monitoramento(id_monitoramento: int, db: Session = Depends(get_db)):
    db_monitoramento = crud.get_monitoramento(db=db, id_monitoramento=id_monitoramento)
    if not db_monitoramento:
        raise HTTPException(status_code=404, detail="Monitoramento não encontrado")
    return db_monitoramento

# Buscar todos os monitoramentos
@router.get("/", response_model=List[MonitoramentoOut])
def read_monitoramentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_monitoramentos(db=db, skip=skip, limit=limit)

# Atualizar monitoramento
@router.put("/{id_monitoramento}", response_model=MonitoramentoOut)
def update_monitoramento(id_monitoramento: int, monitoramento: MonitoramentoUpdate, db: Session = Depends(get_db)):
    db_monitoramento = crud.update_monitoramento(db=db, id_monitoramento=id_monitoramento, monitoramento=monitoramento)
    if not db_monitoramento:
        raise HTTPException(status_code=404, detail="Monitoramento não encontrado")
    return db_monitoramento

# Deletar monitoramento
@router.delete("/{id_monitoramento}")
def delete_monitoramento(id_monitoramento: int, db: Session = Depends(get_db)):
    db_monitoramento = crud.delete_monitoramento(db=db, id_monitoramento=id_monitoramento)
    if not db_monitoramento:
        raise HTTPException(status_code=404, detail="Monitoramento não encontrado")
    return {"message": "Monitoramento deletado com sucesso"}
