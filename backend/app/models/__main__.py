from sqlalchemy import create_engine
from backend.app.database import Base

# Código para testar a conexão ou executar ações no banco de dados
if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://dev_user:Pz8!dH7#sNxLq2Tp@bdmysql.iexpert.net.br:3306/transporte_escolar")
    Base.metadata.create_all(bind=engine)  # Cria as tabelas no banco de dados
    print("Tabelas criadas com sucesso.")
