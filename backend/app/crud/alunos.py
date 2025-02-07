from sqlalchemy.orm import Session
from backend.app.models import Aluno
from backend.app.schemas.alunos import AlunoCreate

def get_aluno(db: Session, aluno_id: int):
    return db.query(Aluno).filter(Aluno.id_aluno == aluno_id).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Aluno).offset(skip).limit(limit).all()

def create_aluno(db: Session, aluno: AlunoCreate):
    db_aluno = Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, aluno_data: AlunoCreate):
    db_aluno = db.query(Aluno).filter(Aluno.id_aluno == aluno_id).first()
    if db_aluno:
        for key, value in aluno_data.dict().items():
            setattr(db_aluno, key, value)
        db.commit()
        db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(Aluno).filter(Aluno.id_aluno == aluno_id).first()
    if db_aluno:
        db.delete(db_aluno)
        db.commit()
    return db_aluno
