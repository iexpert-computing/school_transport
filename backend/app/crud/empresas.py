from sqlalchemy.orm import Session
from backend.app.models.models import Empresa
from backend.app.schemas.empresas import EmpresaCreate

def get_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()

def get_empresas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Empresa).offset(skip).limit(limit).all()

def create_empresa(db: Session, empresa: EmpresaCreate):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def update_empresa(db: Session, empresa_id: int, empresa_data: EmpresaCreate):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        for key, value in empresa_data.dict().items():
            setattr(db_empresa, key, value)
        db.commit()
        db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
    return db_empresa
