# Função para criar um novo contrato
from sqlalchemy.orm import Session
from backend.app.models.models import Contrato
from backend.app.schemas.contratos import ContratoCreate, ContratoUpdate

def create_contrato(db: Session, contrato: ContratoCreate):
    db_contrato = Contrato(
        numero_contrato=contrato.numero_contrato,
        data_inicio=contrato.data_inicio,
        data_fim=contrato.data_fim,
        valor=contrato.valor,
        id_empresa=contrato.id_empresa,
    )
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

# Função para buscar um contrato pelo id
def get_contrato(db: Session, id_contrato: int):
    return db.query(Contrato).filter(Contrato.id_contrato == id_contrato).first()

# Função para buscar todos os contratos
def get_contratos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contrato).offset(skip).limit(limit).all()

# Função para atualizar um contrato
def update_contrato(db: Session, id_contrato: int, contrato: ContratoUpdate):
    db_contrato = db.query(Contrato).filter(Contrato.id_contrato == id_contrato).first()
    if db_contrato:
        db_contrato.numero_contrato = contrato.numero_contrato
        db_contrato.data_inicio = contrato.data_inicio
        db_contrato.data_fim = contrato.data_fim
        db_contrato.valor = contrato.valor
        db_contrato.id_empresa = contrato.id_empresa
        db.commit()
        db.refresh(db_contrato)
    return db_contrato

# Função para deletar um contrato
def delete_contrato(db: Session, id_contrato: int):
    db_contrato = db.query(Contrato).filter(Contrato.id_contrato == id_contrato).first()
    if db_contrato:
        db.delete(db_contrato)
        db.commit()
    return db_contrato