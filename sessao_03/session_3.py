# Sessão 3

# Define a função que faz a análise

def classificar_ativo(valor, status):
    """
    Recebe o valor e status do ativo e retorna a classificação de valor e status operacional.
    """
    #Lógica para classificar o valor
    if valor > 20000.00:
        classificacao_valor = "Alto Valor"
    elif valor >= 5000.00:
        classificacao_valor = "Médio Valor"
    else:
        classificacao_valor = "Baixo Valor"
    
    # Lógica para classificar o status (Versão robusta que fizemos na sessão 2)
    if status == "ativo":
        status_operacional = "Operacional"
    elif status == "manutenção":
        status_operacional = "Em Manutenção"
    elif status == "inativo":
        status_operacional = "Inativo"
    else:
        status_operacional = f"Status Desconhecido: '{status}'"
    
    return status_operacional, classificacao_valor

# --- Código Principal ---

# Os dados do nosso invetário
inventario_completo = [
    {"id": 201, "nome": "Servidor de Aplicação", "status": "ativo", "valor": 25000.00},
    {"id": 202, "nome": "Notebook Engenharia", "status": "ativo", "valor": 12500.50},
    {"id": 203, "nome": "Storage NAS", "status": "inativo", "valor": 8000.00},
    {"id": 204, "nome": "Impressora Fiscal", "status": "manutenção", "valor": 2200.00},
    {"id": 205, "nome": "Switch Core", "status": "desconhecido", "valor": 15000.00}, # Teste do status desconhecido
]

valor_total_inventario = 0.0

print("\n--- Relatório de Ativos (Refatorado com Função) ---")

# O laço 'for' agora é muito mais limpo
for ativo in inventario_completo:
    valor_total_inventario += ativo["valor"]  # Acumula o valor total

    # Chama a função para obter as classificações
    status_operacional, classificacao_valor = classificar_ativo(ativo["valor"], ativo["status"])

    # Imprime o relatório PARA CADA ativo (deve ficar dentro do laço)
    print(f"- Ativo: {ativo['nome']} | Status: {status_operacional} | Classificação: {classificacao_valor}")

print(f"\n>>>> Valor total do inventário: R$ {valor_total_inventario}")