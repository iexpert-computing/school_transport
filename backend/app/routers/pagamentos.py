from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.pagamentos import PagamentoCreate, PagamentoUpdate, PagamentoResponse
from backend.app.database import get_db
from backend.app.crud.pagamentos import (
    create_pagamento,
    get_pagamento,
    get_all_pagamentos,
    update_pagamento,
    delete_pagamento
)
from typing import List

router = APIRouter()

# Criar um novo pagamento
@router.post("/", response_model=PagamentoResponse)
def criar_pagamento(pagamento: PagamentoCreate, db: Session = Depends(get_db)):
    return create_pagamento(db, pagamento.id_contrato, pagamento.valor_pago, pagamento.data_pagamento)

# Obter um pagamento por ID
@router.get("/{pagamento_id}", response_model=PagamentoResponse)
def obter_pagamento(pagamento_id: int, db: Session = Depends(get_db)):
    db_pagamento = get_pagamento(db, pagamento_id=pagamento_id)
    if not db_pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return db_pagamento

# Obter todos os pagamentos
@router.get("/", response_model=List[PagamentoResponse])
def listar_pagamentos(db: Session = Depends(get_db)):
    return get_all_pagamentos(db)

# Atualizar um pagamento
@router.put("/{pagamento_id}", response_model=PagamentoResponse)
def atualizar_pagamento(pagamento_id: int, pagamento: PagamentoUpdate, db: Session = Depends(get_db)):
    db_pagamento = update_pagamento(db, pagamento_id, pagamento.id_contrato, pagamento.valor_pago, pagamento.data_pagamento)
    if not db_pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return db_pagamento

# Deletar um pagamento
@router.delete("/{pagamento_id}")
def deletar_pagamento(pagamento_id: int, db: Session = Depends(get_db)):
    pagamento_excluido = delete_pagamento(db, pagamento_id=pagamento_id)
    if not pagamento_excluido:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return {"msg": "Pagamento excluído com sucesso"}
