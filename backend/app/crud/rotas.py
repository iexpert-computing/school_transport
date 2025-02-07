from sqlalchemy.orm import Session
from backend.app.models.models import Rota
from backend.app.schemas.rotas import RotaCreate, RotaUpdate

def create_rota(db: Session, rota: RotaCreate):
    db_rota = Rota(**rota.dict())
    db.add(db_rota)
    db.commit()
    db.refresh(db_rota)
    return db_rota

def get_rota(db: Session, rota_id: int):
    return db.query(Rota).filter(Rota.id_rota == rota_id).first()

def get_rotas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rota).offset(skip).limit(limit).all()

def update_rota(db: Session, rota_id: int, rota: RotaUpdate):
    db_rota = get_rota(db, rota_id)
    if not db_rota:
        return None
    for key, value in rota.dict(exclude_unset=True).items():
        setattr(db_rota, key, value)
    db.commit()
    db.refresh(db_rota)
    return db_rota

def delete_rota(db: Session, rota_id: int):
    db_rota = get_rota(db, rota_id)
    if not db_rota:
        return None
    db.delete(db_rota)
    db.commit()
    return db_rota
