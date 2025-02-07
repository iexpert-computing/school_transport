from sqlalchemy.orm import Session
from datetime import date
from backend.app.models.models import Condutor
from backend.app.database import SessionLocal

# Função para criar um novo condutor
def create_condutor(db: Session, nome: str, cnh: str, validade_cnh: date, telefone: str = None, id_veiculo: int = None):
    novo_condutor = Condutor(
        nome=nome,
        cnh=cnh,
        validade_cnh=validade_cnh,
        telefone=telefone,
        id_veiculo=id_veiculo,
        status_ativo=True
    )
    db.add(novo_condutor)
    db.commit()
    db.refresh(novo_condutor)
    return novo_condutor

# Função para ler informações de um condutor pelo ID
def get_condutor(db: Session, condutor_id: int):
    return db.query(Condutor).filter(Condutor.id_condutor == condutor_id).first()

# Função para obter todos os condutores
def get_all_condutores(db: Session):
    return db.query(Condutor).all()

# Função para atualizar informações de um condutor
def update_condutor(db: Session, condutor_id: int, nome: str = None, cnh: str = None, validade_cnh: date = None, telefone: str = None, id_veiculo: int = None, status_ativo: bool = None):
    condutor = db.query(Condutor).filter(Condutor.id_condutor == condutor_id).first()
    if not condutor:
        return None
    if nome:
        condutor.nome = nome
    if cnh:
        condutor.cnh = cnh
    if validade_cnh:
        condutor.validade_cnh = validade_cnh
    if telefone:
        condutor.telefone = telefone
    if id_veiculo:
        condutor.id_veiculo = id_veiculo
    if status_ativo is not None:
        condutor.status_ativo = status_ativo
    db.commit()
    db.refresh(condutor)
    return condutor

# Função para deletar um condutor pelo ID
def delete_condutor(db: Session, condutor_id: int):
    condutor = db.query(Condutor).filter(Condutor.id_condutor == condutor_id).first()
    if not condutor:
        return None
    db.delete(condutor)
    db.commit()
    return condutor_id
