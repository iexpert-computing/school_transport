from fastapi import FastAPI
from backend.app.routers import alunos, gestores, veiculos, ponto_embarque, manutencao
from backend.app.routers import condutores, rotas, monitoramento, contratos, empresas

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()

# Registrar as rotas
app.include_router(alunos.router, prefix="/alunos", tags=["alunos"])
app.include_router(gestores.router)
app.include_router(monitoramento.router)
app.include_router(rotas.router, prefix="/rotas", tags=["Rotas"])
app.include_router(contratos.router)
app.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
app.include_router(veiculos.router, prefix="/veiculos", tags=["veiculos"])
app.include_router(ponto_embarque.router, prefix="/pontos_embarque", tags=["Pontos de Embarque"])
app.include_router(manutencao.router, prefix="/manutencao", tags=["Manutenção"])
app.include_router(condutores.router, prefix="/condutores", tags=["Condutores"])
app.include_router(pagamentos.router, prefix="/pagamentos", tags=["Pagamentos"])



@app.get("/")
def read_root():
    return {"message": "Sistema de Transporte Escolar"}
