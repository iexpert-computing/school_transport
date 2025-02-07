from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexão com o banco de dados MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://dev_user:Pz8!dH7#sNxLq2Tp@bdmysql.iexpert.net.br:3306/transporte_escolar"

# Criação do motor (engine) com a string de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)  # Remova connect_args={"check_same_thread": False}

# Criando uma sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Exemplo de como usar a sessão para realizar operações
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Código para verificar a conexão e imprimir "OK" no console
if __name__ == "__main__":
    try:
        with SessionLocal() as session:
            # Executando uma consulta simples para testar a conexão
            session.execute(text("SELECT 1"))
            print("Conexão com o banco de dados estabelecida com sucesso. OK!")
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
