import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# String de conexão com o banco de dados PostgreSQL
# Formato: "postgresql://usuario:senha@host:porta/nome_do_banco"
# Por enquanto, vamos deixar os dados aqui. No futuro, isso irá para um arquivo de configuração

DATABASE_URL = os.getenv("DATABASE_URL")

# O 'engine' é o ponto de entrada central para a comunicação com o banco.
engine = create_engine(DATABASE_URL)

def criar_banco_e_tabelas():
    # Esta função mágica pega todos os modelos que herdam de SQLModel
    # e cria as tabelas correspondentes no banco de dados.
    SQLModel.metadata.create_all(engine)