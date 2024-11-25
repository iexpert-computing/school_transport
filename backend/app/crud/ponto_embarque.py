# backend/app/crud/ponto_embarque.py

from sqlalchemy.orm import Session
from backend.app.models.models import PontoEmbarque
from backend.app.schemas.ponto_embarque import PontoEmbarqueCreate, PontoEmbarqueUpdate, PontoEmbarqueOut

# CREATE
def create_ponto_embarque(db: Session, ponto_embarque: PontoEmbarqueCreate):
    db_ponto = PontoEmbarque(
        endereco_ponto=ponto_embarque.endereco_ponto,
        latitude=ponto_embarque.latitude,
        longitude=ponto_embarque.longitude
    )
    db.add(db_ponto)
    db.commit()
    db.refresh(db_ponto)
    return db_ponto

# READ ALL
def get_pontos_embarque(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PontoEmbarque).offset(skip).limit(limit).all()

# READ BY ID
def get_ponto_embarque(db: Session, ponto_id: int):
    return db.query(PontoEmbarque).filter(PontoEmbarque.id_ponto == ponto_id).first()

# UPDATE
def update_ponto_embarque(db: Session, ponto_id: int, ponto_embarque: PontoEmbarqueUpdate):
    db_ponto = db.query(PontoEmbarque).filter(PontoEmbarque.id_ponto == ponto_id).first()
    if not db_ponto:
        return None
    db_ponto.endereco_ponto = ponto_embarque.endereco_ponto
    db_ponto.latitude = ponto_embarque.latitude
    db_ponto.longitude = ponto_embarque.longitude
    db.commit()
    db.refresh(db_ponto)
    return db_ponto

# DELETE
def delete_ponto_embarque(db: Session, ponto_id: int):
    db_ponto = db.query(PontoEmbarque).filter(PontoEmbarque.id_ponto == ponto_id).first()
    if db_ponto:
        db.delete(db_ponto)
        db.commit()
    return db_ponto
