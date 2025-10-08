from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_lenght=100)
    matricula: str = Field(max_lenght=10, unique=True, index=True)
    tipo_usuario: str = Field(max_lenght=20)
    senhas_hash: str

    # A "mágica" do relacionamento:
    # Este atributo 'logs' não existe como uma coluna no banco.
    # É um campo "virtual" que o ORM vai preencher para nós com
    # uma lista de todos os logs que pertencem a este usuário.
    logs: List["LogDeAcesso"] = Relationship(back_populates="usuario")

class Area(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_area: str = Field(index=True)
    descricao: Optional[str] = None
    dupla_custodia: bool = Field(default=False)

    logs: List["LogDeAcesso"] = Relationship(back_populates="area")

class LogDeAcesso(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(index=True)
    tipo_evento: str

    #Chaves Estrangeiras
    usuario_id: int = Field(foreign_key="usuario.id")
    area_id: int = Field(foreign_key="area.id")

    #Criando a outra ponta do relacionamento
    #back_populates aponta para o nome do atributo na outra classe
    usuario: Usuario = Relationship(back_populates="logs")
    area: Area = Relationship(back_populates="logs")
