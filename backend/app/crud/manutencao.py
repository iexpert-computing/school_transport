from sqlalchemy.orm import Session
from backend.app.models.models import Manutencao
from backend.app.schemas.manutencao import ManutencaoCreate

def create_manutencao(db: Session, manutencao: ManutencaoCreate):
    db_manutencao = Manutencao(**manutencao.dict())
    db.add(db_manutencao)
    db.commit()
    db.refresh(db_manutencao)
    return db_manutencao

def get_manutencao(db: Session, manutencao_id: int):
    return db.query(Manutencao).filter(Manutencao.id_manutencao == manutencao_id).first()

def get_manutencoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Manutencao).offset(skip).limit(limit).all()

def update_manutencao(db: Session, manutencao_id: int, manutencao_data: ManutencaoCreate):
    db_manutencao = db.query(Manutencao).filter(Manutencao.id_manutencao == manutencao_id).first()
    if db_manutencao:
        for key, value in manutencao_data.dict().items():
            setattr(db_manutencao, key, value)
        db.commit()
        db.refresh(db_manutencao)
    return db_manutencao

def delete_manutencao(db: Session, manutencao_id: int):
    db_manutencao = db.query(Manutencao).filter(Manutencao.id_manutencao == manutencao_id).first()
    if db_manutencao:
        db.delete(db_manutencao)
        db.commit()
    return db_manutencao
