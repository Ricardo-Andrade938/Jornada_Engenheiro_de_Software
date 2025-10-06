# # Session 2

# # --- 1. Estruturas de Condicionais ---

# asset_cost = 5000.00
# asset_status = "Ativo"

# print("---Análise de Ativo ---")

# # A instrução 'if' verifica se uma condição é verdadeira
# if asset_cost > 10000.00:
#     print("Classificação: Ativo de Alto Valor")

# # 'elif' (else if) verifica outra condição se a primeira for falsa
# elif asset_cost > 2500.00:
#     print("Classificação: Ativo de Médio Valor")

# # 'else' é executado se todas as condições anteriores forem falsas
# else:
#     print("Classificação: Ativo de Baixo Valor")

# # Podemos combinar condições com 'and' e 'or'
# if asset_cost > 4000.00 and asset_status == "Ativo":
#     print("Status: Ativo de alto valor. Recomendar seguro.")

# # --- 2. Laço de Repetição 'for' ---
# # Uma lista em python é definida por colchetes []
# asset_name = ["Notebook Dell", "Servidor HP", "Switch Cisco", "Roteador TP-Link"]

# print("\n--- Inventário de Ativos ---")
# # Este laço vai passar por cada item da lista 'asset_names'
# # A cada "passada", o item atal será colocado na variavel 'asset'
# for asset in asset_name:
#     print(f"Item: {asset}")

# # Exemplo mais complexo: uma lista de dicionários (muito comum!)
# # Um dicionário em Python usa {} para pares "chave": valor
# inventory = [
#     {"id": 101, "name": "Notebook Dell", "status": "ativo"},
#     {"id": 102, "name": "Servidor HP", "status": "manutenção"},
#     {"id": 103, "name": "Switch Cisco", "status": "ativo"},
# ]

# print("\n---Relatório de Status ---")
# for item in inventory:
#     # Acessamos os valores do dicionário usando as chaves
#     if item["status"] == "manutenção":
#             print(f"ALERTA: O ativo '{item['name']}' (ID: {item['id']}) precisa de atenção.")

# # --- 3. Laço de Repetição 'while' ---

# # Exemplo de um menu simples
# print("\n--- Sistema de Autenticação ---")
# user_input = ""
# tentativas = 0
# max_tentativas = 3

# while user_input != "sair" and tentativas < max_tentativas:
#     user_input = input("Digite a senha ou 'sair' para terminar:")
#     if user_input == "senha123":
#         print("Acesso concedido.")
#         break # O 'Break' encerra o laço imediatamente
#     else:
#         tentativas += 1 # O mesmo que tentativas = tentativas +1
#         print(f"Senha incorreta. Tentativas restantes: {max_tentativas - tentativas}")

# --- EXERCÍCIO FINAL DA SESSÃO 2 ---
# Agora, junte tudo. Crie um script que:

# Tenha uma lista de ativos (como a lista inventory que usamos). Adicione um campo de valor a cada um.

# Use um laço for para percorrer a lista.

# Use if/elif/else para imprimir uma análise de cada ativo (ex: se o valor for alto, se está ativo ou não).

# Calcule e, ao final, imprima o valor total de todos os ativos no inventário.

# Exemplo de como começar:

print("\n--- Relatório Financeiro e Operacional de Ativos ---")

inventario_completo = [
    {"id": 201, "nome": "Servidor de Aplicação", "status": "ativo", "valor": 25000.00},
    {"id": 202, "nome": "Notebook Engenharia", "status": "ativo", "valor": 12500.50},
    {"id": 203, "nome": "Storage NAS", "status": "inativo", "valor": 8000.00},
    {"id": 204, "nome": "Impressora Fiscal", "status": "manutenção", "valor": 2200.00},
]

valor_total_inventario = 0.0

for ativo in inventario_completo:
    valor_total_inventario += ativo["valor"]  # Acumula o valor total

    # Análise do Ativo
    if ativo["valor"] > 20000.00:
        classificacao_valor = "Alto Valor"
    elif ativo["valor"] >= 5000.00:
        classificacao_valor = "Médio_Valor"
    else:
        classificacao_valor = "Baixo Valor"

    if ativo["status"] == "ativo":
        status_operacional = "Operacional"
    elif ativo["status"] == "manutenção":
        status_operacional = "Em Manutenção"
    elif ativo["status"] == "inativo":
        status_operacional = "Inativo"
    else:
        status_operacional = "Status Desconhecido"
    # 3. Imprime o relatório PARA CADA ativo (deve ficar dentro do laço)
    print(f"- Ativo: {ativo['nome']} | Status: {status_operacional} | Classificação: {classificacao_valor}")

print(f"\n>>>> Valor total do inventário: R$ {valor_total_inventario}")

# refatore o código acima para usar uma função que calcula a classificação



