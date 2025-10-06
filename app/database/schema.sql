CREATE TABLE usuarios(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    tipo_usuario VARCHAR(20) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL
);

CREATE TABLE areas(
    id SERIAL PRIMARY KEY,
    nome_area VARCHAR(100) NOT NULL,
    descricao TEXT,
    dupla_custodia BOOLEAN DEFAULT FALSE
);

CREATE TABLE logs_de_acesso(
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
    tipo_evento VARCHAR(50) NOT NULL,
    usuario_id INTEGER REFERENCES usuarios(id),
    area_id INTEGER REFERENCES areas(id),
    detalhes TEXT
)

