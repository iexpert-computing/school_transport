from sqlalchemy.orm import Session
from backend.app.models.models import Pagamento

def create_pagamento(db: Session, id_contrato: int, valor_pago: float, data_pagamento: str):
    db_pagamento = Pagamento(id_contrato=id_contrato, valor_pago=valor_pago, data_pagamento=data_pagamento)
    db.add(db_pagamento)
    db.commit()
    db.refresh(db_pagamento)
    return db_pagamento

def get_pagamento(db: Session, pagamento_id: int):
    return db.query(Pagamento).filter(Pagamento.id_pagamento == pagamento_id).first()

def get_all_pagamentos(db: Session):
    return db.query(Pagamento).all()

def update_pagamento(db: Session, pagamento_id: int, id_contrato: int, valor_pago: float, data_pagamento: str):
    db_pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == pagamento_id).first()
    if db_pagamento:
        db_pagamento.id_contrato = id_contrato
        db_pagamento.valor_pago = valor_pago
        db_pagamento.data_pagamento = data_pagamento
        db.commit()
        db.refresh(db_pagamento)
    return db_pagamento

def delete_pagamento(db: Session, pagamento_id: int):
    db_pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == pagamento_id).first()
    if db_pagamento:
        db.delete(db_pagamento)
        db.commit()
        return True
    return False
