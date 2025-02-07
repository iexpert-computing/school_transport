from sqlalchemy.orm import Session
from backend.app.models import Veiculo
from backend.app.schemas.veiculos import VeiculoCreate

def get_veiculo(db: Session, veiculo_id: int):
    return db.query(Veiculo).filter(Veiculo.id_veiculo == veiculo_id).first()

def get_veiculos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Veiculo).offset(skip).limit(limit).all()

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    db_veiculo = Veiculo(**veiculo.dict())
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def update_veiculo(db: Session, veiculo_id: int, veiculo_data: VeiculoCreate):
    db_veiculo = db.query(Veiculo).filter(Veiculo.id_veiculo == veiculo_id).first()
    if db_veiculo:
        for key, value in veiculo_data.dict().items():
            setattr(db_veiculo, key, value)
        db.commit()
        db.refresh(db_veiculo)
    return db_veiculo

def delete_veiculo(db: Session, veiculo_id: int):
    db_veiculo = db.query(Veiculo).filter(Veiculo.id_veiculo == veiculo_id).first()
    if db_veiculo:
        db.delete(db_veiculo)
        db.commit()
    return db_veiculo
