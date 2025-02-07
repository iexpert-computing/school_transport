from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.condutores import CondutorCreate, CondutorUpdate, CondutorResponse
from backend.app.database import get_db
from backend.app.crud.condutores import (
    create_condutor,
    get_condutor,
    get_all_condutores,
    update_condutor,
    delete_condutor
)
from typing import List

router = APIRouter()

# Criar um novo condutor
@router.post("/", response_model=CondutorResponse)
def criar_condutor(condutor: CondutorCreate, db: Session = Depends(get_db)):
    return create_condutor(
        db,
        nome=condutor.nome,
        cnh=condutor.cnh,
        validade_cnh=condutor.validade_cnh,
        telefone=condutor.telefone,
        id_veiculo=condutor.id_veiculo
    )

# Obter um condutor por ID
@router.get("/{condutor_id}", response_model=CondutorResponse)
def obter_condutor(condutor_id: int, db: Session = Depends(get_db)):
    db_condutor = get_condutor(db, condutor_id=condutor_id)
    if not db_condutor:
        raise HTTPException(status_code=404, detail="Condutor não encontrado")
    return db_condutor

# Obter todos os condutores
@router.get("/", response_model=List[CondutorResponse])  # Corrigido para usar List
def listar_condutores(db: Session = Depends(get_db)):
    return get_all_condutores(db)

# Atualizar um condutor
@router.put("/{condutor_id}", response_model=CondutorResponse)
def atualizar_condutor(condutor_id: int, condutor: CondutorUpdate, db: Session = Depends(get_db)):
    db_condutor = update_condutor(
        db,
        condutor_id=condutor_id,
        nome=condutor.nome,
        cnh=condutor.cnh,
        validade_cnh=condutor.validade_cnh,
        telefone=condutor.telefone,
        id_veiculo=condutor.id_veiculo,
        status_ativo=condutor.status_ativo
    )
    if not db_condutor:
        raise HTTPException(status_code=404, detail="Condutor não encontrado")
    return db_condutor

# Deletar um condutor
@router.delete("/{condutor_id}")
def deletar_condutor(condutor_id: int, db: Session = Depends(get_db)):
    condutor_excluido = delete_condutor(db, condutor_id=condutor_id)
    if not condutor_excluido:
        raise HTTPException(status_code=404, detail="Condutor não encontrado")
    return {"msg": "Condutor excluído com sucesso"}
