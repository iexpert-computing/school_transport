from sqlalchemy.orm import Session
from backend.app.models import Monitoramento
from backend.app.schemas.monitoramento import MonitoramentoCreate, MonitoramentoUpdate

# Função para criar um novo monitoramento
def create_monitoramento(db: Session, monitoramento: MonitoramentoCreate):
    db_monitoramento = Monitoramento(
        id_veiculo=monitoramento.id_veiculo,
        data_hora=monitoramento.data_hora,
        localizacao=monitoramento.localizacao,
        evento=monitoramento.evento
    )
    db.add(db_monitoramento)
    db.commit()
    db.refresh(db_monitoramento)
    return db_monitoramento

# Função para buscar um monitoramento pelo id
def get_monitoramento(db: Session, id_monitoramento: int):
    return db.query(Monitoramento).filter(Monitoramento.id_monitoramento == id_monitoramento).first()

# Função para buscar todos os monitoramentos
def get_monitoramentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Monitoramento).offset(skip).limit(limit).all()

# Função para atualizar um monitoramento
def update_monitoramento(db: Session, id_monitoramento: int, monitoramento: MonitoramentoUpdate):
    db_monitoramento = db.query(Monitoramento).filter(Monitoramento.id_monitoramento == id_monitoramento).first()
    if db_monitoramento:
        db_monitoramento.id_veiculo = monitoramento.id_veiculo
        db_monitoramento.data_hora = monitoramento.data_hora
        db_monitoramento.localizacao = monitoramento.localizacao
        db_monitoramento.evento = monitoramento.evento
        db.commit()
        db.refresh(db_monitoramento)
    return db_monitoramento

# Função para deletar um monitoramento
def delete_monitoramento(db: Session, id_monitoramento: int):
    db_monitoramento = db.query(Monitoramento).filter(Monitoramento.id_monitoramento == id_monitoramento).first()
    if db_monitoramento:
        db.delete(db_monitoramento)
        db.commit()
    return db_monitoramento
