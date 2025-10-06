# app/schemas.py

# Importamos datetime para lidar com timestamps e Optional para campos que podem ser nulos
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Schema para a representação de um Usuário na API
class Usuario(BaseModel):
    id: int
    nome: str
    matricula: str
    tipo_usuario: str
    

# Schema para a representação de uma Área na API
class Area(BaseModel):
    id: int
    nome_area: str
    descricao: Optional[str] = None
    dupla_custodia: bool = False

# Schema para a representação de um Log de Acesso na API
class LogDeAcesso(BaseModel):
    id: int
    timestamp: datetime
    tipo_evento: str
    usuario_id: int
    area_id: int
    detalhes: Optional[str] = None