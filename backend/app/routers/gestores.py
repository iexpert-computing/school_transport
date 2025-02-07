from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.gestores import GestorCreate, GestorOut
from backend.app.database import get_db
from backend.app.crud.gestores import create_gestor, get_gestor, get_gestores, update_gestor, delete_gestor
from typing import List

router = APIRouter()

# Criar gestor
@router.post("/", response_model=GestorOut)
def create_gestor_endpoint(gestor: GestorCreate, db: Session = Depends(get_db)):
    return create_gestor(db=db, gestor=gestor)

# Ler gestor por ID
@router.get("/{gestor_id}", response_model=GestorOut)
def read_gestor(gestor_id: int, db: Session = Depends(get_db)):
    db_gestor = get_gestor(db, gestor_id=gestor_id)
    if db_gestor is None:
        raise HTTPException(status_code=404, detail="Gestor não encontrado")
    return db_gestor

# Ler todos os gestores
@router.get("/", response_model=List[GestorOut])
def read_gestores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_gestores(db, skip=skip, limit=limit)

# Atualizar gestor
@router.put("/{gestor_id}", response_model=GestorOut)
def update_gestor_endpoint(gestor_id: int, gestor: GestorCreate, db: Session = Depends(get_db)):
    db_gestor = update_gestor(db, gestor_id=gestor_id, gestor_data=gestor)
    if db_gestor is None:
        raise HTTPException(status_code=404, detail="Gestor não encontrado")
    return db_gestor

# Deletar gestor
@router.delete("/{gestor_id}", response_model=GestorOut)
def delete_gestor_endpoint(gestor_id: int, db: Session = Depends(get_db)):
    db_gestor = delete_gestor(db, gestor_id=gestor_id)
    if db_gestor is None:
        raise HTTPException(status_code=404, detail="Gestor não encontrado")
    return db_gestor
