from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from app import models
from app.database.database import criar_banco_e_tabelas, engine
from app.models import \
    Usuario as UsuarioModel  # Renomeia para evitar conflito com o schema
from app.schemas import UsuarioCreate, UsuarioRead

# O "lifespan" gerencia o que acontece na inicialização e no desligamento da API

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a API...")
    print("Conectando ao banco de dados e criando tabelas, se necessário...")

    # Executa a função que cria as tabelas
    criar_banco_e_tabelas()

    print("Startup finalizando.")
    yield
    print("Desligando a API...")

app = FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def ler_raiz():
    return {"message": "API de Controle de Acesso rodando!"}

#--- Novo Endpoint ---

@app.post("/usuarios/", response_model=UsuarioRead, status_code=201)
def create_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    """Cria um novo usuário no sistema."""

    #1. Cria ua instância do modelo do banco (UsuarioModel) a partir dos dados criados do schema de entrada (UsuarioCreate)
    db_usuario = UsuarioModel.model_validate(usuario)

    #2. Adiciona o novo objeto à sessão do banco de dados
    session.add(db_usuario)

    #3. Confirma a transação salvando o objeto no banco
    session.commit()

    #4 Atualiza o objeto 'db_usuario' com os dados que o banco gerou (como o 'id')
    session.refresh(db_usuario)

    #5. Retorna o objeto criado, que o FastAPI converterá para o schema 'UsuarioRead'
    return db_usuario