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

-- Inserindo dados de exemplo para podermos consultar
INSERT INTO usuarios (nome, matricula, tipo_usuario, senha_hash) VALUES
('Ricardo Andrade', 'M00938', 'admin', 'hash_da_senha_1'),
('Ana Clara', 'M00101', 'operador', 'hash_da_senha_2');

INSERT INTO areas (nome_area, descricao, dupla_custodia) VALUES
('Data Center Principal', 'Sala dos racks 01-10', TRUE),
('Recepção', 'Entrada principal do prédio', FALSE);

-- Vamos simular dois eventos de acesso
INSERT INTO logs_de_acesso (tipo_evento, usuario_id, area_id, detalhes) VALUES
('entrada_autorizada', 1, 1, 'Acesso à sala de servidores.'),
('acesso_negado', 2, 1, 'Tentativa de acesso a área restrita sem permissão.');

-- TAREFA 1: Escreva a consulta com JOIN aqui.
-- Dica: Você precisará fazer JOIN da tabela 'logs_de_acesso' com a 'usuarios'
-- E TAMBÉM com a 'areas'. Sim, você pode ter múltiplos JOINs em uma consulta!
-- A estrutura seria: FROM logs_de_acesso JOIN usuarios ON ... JOIN areas ON ...

SELECT
    usuarios.id,
    usuarios.nome AS nome_usuario,
    areas.nome_area,
    logs_de_acesso.tipo_evento,
    logs_de_acesso.timestamp
FROM logs_de_acesso
INNER JOIN usuarios ON logs_de_acesso.usuario_id = usuarios.id
INNER JOIN areas ON logs_de_acesso.area_id = areas.id;

-- TAREFA 2: Escreva o comando para criar um índice na coluna 'timestamp' da tabela 'logs_de_acesso'.
CREATE INDEX idx_timestamp ON logs_de_acesso(timestamp);

-- TAREFA 3: Escreva um bloco de transação para a seguinte operação:
-- "Registrar um log de 'saida_autorizada' do usuário 'Ana Clara' (ID 2) da 'Recepção' (ID 2) E,
--  ao mesmo tempo, registrar um log de 'entrada_autorizada' para a mesma usuária na área 'Data Center Principal' (ID 1)".
-- Se uma falhar, a outra deve ser desfeita.

-- BEGIN;
-- INSERT INTO logs_de_acesso... (primeiro log)
-- INSERT INTO logs_de_acesso... (segundo log)
-- COMMIT;

BEGIN;
INSERT INTO logs_de_acesso (tipo_evento, usuario_id, area_id, detalhes) VALUES
('saida_autorizada', 2, 2, 'Saída da recepção.');
INSERT INTO logs_de_acesso (tipo_evento, usuario_id, area_id, detalhes) VALUES
('entrada_autorizada', 2, 1, 'Entrada na sala de servidores.');
COMMIT;