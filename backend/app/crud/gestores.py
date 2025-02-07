from sqlalchemy.orm import Session
from backend.app.models import Gestor
from backend.app.schemas.gestores import GestorCreate

# Criar gestor
def create_gestor(db: Session, gestor: GestorCreate):
    db_gestor = Gestor(
        nome=gestor.nome,
        email=gestor.email,
        senha_hash=gestor.senha_hash,
        nivel_acesso=gestor.nivel_acesso,
        status_ativo=gestor.status_ativo
    )
    db.add(db_gestor)
    db.commit()
    db.refresh(db_gestor)
    return db_gestor

# Ler gestor por ID
def get_gestor(db: Session, gestor_id: int):
    return db.query(Gestor).filter(Gestor.id_gestor == gestor_id).first()

# Ler todos os gestores
def get_gestores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Gestor).offset(skip).limit(limit).all()

# Atualizar gestor
def update_gestor(db: Session, gestor_id: int, gestor_data: GestorCreate):
    db_gestor = db.query(Gestor).filter(Gestor.id_gestor == gestor_id).first()
    if db_gestor:
        db_gestor.nome = gestor_data.nome
        db_gestor.email = gestor_data.email
        db_gestor.senha_hash = gestor_data.senha_hash
        db_gestor.nivel_acesso = gestor_data.nivel_acesso
        db_gestor.status_ativo = gestor_data.status_ativo
        db.commit()
        db.refresh(db_gestor)
    return db_gestor

# Deletar gestor
def delete_gestor(db: Session, gestor_id: int):
    db_gestor = db.query(Gestor).filter(Gestor.id_gestor == gestor_id).first()
    if db_gestor:
        db.delete(db_gestor)
        db.commit()
    return db_gestor
