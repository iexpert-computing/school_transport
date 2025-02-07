from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.alunos import AlunoCreate, AlunoOut
from backend.app.crud.alunos import get_aluno, get_alunos, create_aluno, update_aluno, delete_aluno
from backend.app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=AlunoOut)

def create_aluno_route(aluno: AlunoCreate, db: Session = Depends(get_db)):
    return create_aluno(db, aluno)

@router.get("/{aluno_id}", response_model=AlunoOut)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@router.get("/", response_model=List[AlunoOut])
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_alunos(db, skip=skip, limit=limit)

@router.put("/{aluno_id}", response_model=AlunoOut)
def update_aluno_route(aluno_id: int, aluno_data: AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = update_aluno(db, aluno_id, aluno_data)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@router.delete("/{aluno_id}", response_model=AlunoOut)
def delete_aluno_route(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = delete_aluno(db, aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno
