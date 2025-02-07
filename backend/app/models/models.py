from sqlalchemy import ForeignKey, DateTime, Time, Text, Numeric, Column, Integer, String, Boolean, Date, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLAEnum  # SQLAlchemy Enum para uso nas colunas
from backend.app.database import Base
from enum import Enum  # Enum para criação de classes de tipos enumerados

# Classe Aluno
class Aluno(Base):
    __tablename__ = 'alunos'

    id_aluno = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco = Column(String(255))
    telefone = Column(String(15))
    id_ponto_embarque = Column(Integer, ForeignKey('pontos_embarque.id_ponto'))
    necessidade_especial = Column(Boolean, default=False)
    status_ativo = Column(Boolean, default=True)

    ponto_embarque = relationship("PontoEmbarque", back_populates="alunos")

# Enum para níveis de acesso
class NivelAcessoEnum(str, Enum):
    admin = "admin"
    gerente = "gerente"
    operador = "operador"

# Classe Gestor
class Gestor(Base):
    __tablename__ = "gestores"

    id_gestor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    nivel_acesso = Column(SQLAEnum(NivelAcessoEnum), nullable=False)
    status_ativo = Column(Boolean, default=True)

# Classe Condutor
class Condutor(Base):
    __tablename__ = 'condutores'
    __table_args__ = {'extend_existing': True}

    id_condutor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cnh = Column(String(20), unique=True, nullable=False)
    validade_cnh = Column(Date, nullable=False)
    telefone = Column(String(15))
    id_veiculo = Column(Integer, ForeignKey("veiculos.id_veiculo"))
    status_ativo = Column(Boolean, default=True)

    veiculo = relationship("Veiculo", back_populates="condutores")

# Enum para status do veículo
class StatusVeiculoEnum(str, Enum):
    ativo = 'ativo'
    inativo = 'inativo'
    manutencao = 'manutencao'

# Classe Veiculo
class Veiculo(Base):
    __tablename__ = 'veiculos'

    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(100), nullable=False)
    placa = Column(String(10), nullable=False, unique=True)
    ano = Column(Integer, nullable=False)
    capacidade = Column(Integer, nullable=False)
    status_veiculo = Column(SQLAEnum(StatusVeiculoEnum), default=StatusVeiculoEnum.ativo)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa'))

    empresa = relationship("Empresa", back_populates="veiculos")
    condutores = relationship("Condutor", back_populates="veiculo")

# Enum para status da rota
class StatusRotaEnum(str, Enum):
    ativa = 'ativa'
    inativa = 'inativa'

# Classe Rota
class Rota(Base):
    __tablename__ = "rotas"

    id_rota = Column(Integer, primary_key=True, autoincrement=True)
    nome_rota = Column(String(100), nullable=False)
    distancia_total = Column(DECIMAL(10, 2))
    duracao_prevista = Column(Time)
    id_condutor = Column(Integer, ForeignKey("condutores.id_condutor"))
    id_veiculo = Column(Integer, ForeignKey("veiculos.id_veiculo"))
    status_rota = Column(SQLAEnum(StatusRotaEnum), default=StatusRotaEnum.ativa)

    condutor = relationship("Condutor", back_populates="rotas")
    veiculo = relationship("Veiculo", back_populates="rotas")

# Classe PontoEmbarque
class PontoEmbarque(Base):
    __tablename__ = "pontos_embarque"

    id_ponto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    endereco_ponto = Column(String(255), nullable=False)
    latitude = Column(DECIMAL(9, 6), nullable=False)
    longitude = Column(DECIMAL(9, 6), nullable=False)

    alunos = relationship("Aluno", back_populates="ponto_embarque")

# Classe Contrato
class Contrato(Base):
    __tablename__ = 'contratos'

    id_contrato = Column(Integer, primary_key=True, index=True)
    numero_contrato = Column(String(50), unique=True, nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor = Column(DECIMAL(15, 2), nullable=False)
    id_empresa = Column(Integer, ForeignKey("empresas.id_empresa"))

    empresa = relationship("Empresa", back_populates="contratos")

# Classe Monitoramento
class Monitoramento(Base):
    __tablename__ = 'monitoramento'

    id_monitoramento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_veiculo = Column(Integer, ForeignKey('veiculos.id_veiculo'), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    localizacao = Column(String(255))
    evento = Column(String(255))

    veiculo = relationship("Veiculo", back_populates="monitoramentos")

# Classe Empresa
class Empresa(Base):
    __tablename__ = 'empresas'

    id_empresa = Column(Integer, primary_key=True, autoincrement=True)
    nome_empresa = Column(String(100), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    telefone = Column(String(15))
    email_empresa = Column(String(100))

    veiculos = relationship("Veiculo", back_populates="empresa")
    contratos = relationship("Contrato", back_populates="empresa")

# Enum para tipo de manutenção
class TipoManutencaoEnum(str, Enum):
    preventiva = 'preventiva'
    corretiva = 'corretiva'

# Classe Manutencao
class Manutencao(Base):
    __tablename__ = "manutencao"

    id_manutencao = Column(Integer, primary_key=True, autoincrement=True)
    id_veiculo = Column(Integer, ForeignKey("veiculos.id_veiculo"))
    data_manutencao = Column(Date, nullable=False)
    tipo_manutencao = Column(SQLAEnum(TipoManutencaoEnum), nullable=False)
    descricao = Column(Text)
    custo = Column(Numeric(10, 2))

    veiculo = relationship("Veiculo", back_populates="manutencao")

class Pagamento(Base):
    __tablename__ = 'pagamentos'

    id_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    id_contrato = Column(Integer, ForeignKey('contratos.id_contrato'))
    valor_pago = Column(DECIMAL(15, 2), nullable=False)
    data_pagamento = Column(Date, nullable=False)

    # Relacionamento com a tabela Contrato
    contrato = relationship("Contrato", back_populates="pagamentos")
