# #String (str): Para textos
# asset_name = "Servidor Dell powerEdge T350"
# asset_location = "Data Center Principal"

# # Integer (int): Para números inteiros
# asset_id = 202501
# rack_unit = 4

# # Float (float): Para números com casas decimais
# asset_cost = 17399.00

# # Boolean (bool): Para valores verdadeiros ou falsos
# is_critical = True

# print(f"Cadastrando ativo: {asset_name} (ID: {asset_id})")

# # Operadores Aritméticos
# buy_quantity = 5
# total_investiment = asset_cost * buy_quantity
# print(f"Custo total para {buy_quantity} unidades: R$ {total_investiment}")

# # Operadores de Comparação
# is_over_budget = total_investiment > 80000.00
# print(f"O investimento excede o orçamento? {is_over_budget}")

# --- EXERCÍCIO FINAL DA SESSÃO 1 ---

print("\n--- Calculadora de Custo de Ativos de TI ---")

# A função input() captura dados do usuário como string
item_name = input("Digite o nome do ativo: ")
item_cost_str = input("Digite o custo unitário do ativo: ")
item_qty_str = input("Digite a quantidade: ")

# Precisamos converter as strings para os tipos numéricos corretos
item_cost = float(item_cost_str)
item_qty = int(item_qty_str)

# Cálculo
final_total_cost = item_cost * item_qty

# Exibição do resultado formatado com F-strings
print("\n--- Resumo do Investimento ---")
print(f"Ativo: {item_name}")
print(f"Custo Unitário: R$ {item_cost}")
print(f"Quantidade: {item_qty}")
print(f"Custo Total: R$ {final_total_cost}")