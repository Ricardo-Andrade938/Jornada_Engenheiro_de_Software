from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import criar_banco_e_tabelas

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

@app.get("/")
def ler_raiz():
    return {"message": "API de Controle de Acesso rodando!"}