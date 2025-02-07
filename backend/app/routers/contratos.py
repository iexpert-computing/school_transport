from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app import crud
from backend.app.schemas.contratos import ContratoCreate, ContratoUpdate, ContratoOut

from backend.app.database import get_db

router = APIRouter(
    prefix="/contratos",
    tags=["contratos"],
)

# Criar novo contrato
@router.post("/", response_model=schemas.ContratoOut)
def create_contrato(contrato: schemas.ContratoCreate, db: Session = Depends(get_db)):
    return crud.create_contrato(db=db, contrato=contrato)

# Buscar contrato por id
@router.get("/{id_contrato}", response_model=schemas.ContratoOut)
def read_contrato(id_contrato: int, db: Session = Depends(get_db)):
    db_contrato = crud.get_contrato(db=db, id_contrato=id_contrato)
    if not db_contrato:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return db_contrato

# Buscar todos os contratos
@router.get("/", response_model=list[schemas.ContratoOut])
def read_contratos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_contratos(db=db, skip=skip, limit=limit)

# Atualizar contrato
@router.put("/{id_contrato}", response_model=schemas.ContratoOut)
def update_contrato(id_contrato: int, contrato: schemas.ContratoUpdate, db: Session = Depends(get_db)):
    db_contrato = crud.update_contrato(db=db, id_contrato=id_contrato, contrato=contrato)
    if not db_contrato:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return db_contrato

# Deletar contrato
@router.delete("/{id_contrato}")
def delete_contrato(id_contrato: int, db: Session = Depends(get_db)):
    db_contrato = crud.delete_contrato(db=db, id_contrato=id_contrato)
    if not db_contrato:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return {"message": "Contrato deletado com sucesso"}
