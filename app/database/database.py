from sqlmodel import SQLModel, create_engine

# String de conexão com o banco de dados PostgreSQL
# Formato: "postgresql://usuario:senha@host:porta/nome_do_banco"
# Por enquanto, vamos deixar os dados aqui. No futuro, isso irá para um arquivo de configuração

DATABASE_URL = "postgresql://seu_usuario: sua_senha@localhost:5432/seu_banco"

# O 'engine' é o ponto de entrada central para a comunicação com o banco.
engine = create_engine(DATABASE_URL)

def criar_banco_e_tabelas():
    # Esta função mágica pega todos os modelos que herdam de SQLModel
    # e cria as tabelas correspondentes no banco de dados.
    SQLModel.metada.create_all(engine)