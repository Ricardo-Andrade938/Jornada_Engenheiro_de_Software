# session_3_exercicio.py

# DADOS DE ENTRADA (pode copiar e colar esta lista)
lista_de_usuarios = [
    {"id": 1, "nome": "Carlos Silva", "nivel_acesso": "admin", "ultimo_login_dias": 5},
    {"id": 2, "nome": "Mariana Souza", "nivel_acesso": "usuario", "ultimo_login_dias": 120},
    {"id": 3, "nome": "Fernando Lima", "nivel_acesso": "usuario", "ultimo_login_dias": 30},
    {"id": 4, "nome": "Juliana Pereira", "nivel_acesso": "gestor", "ultimo_login_dias": 15},
    {"id": 5, "nome": "Ricardo Alves", "nivel_acesso": "admin", "ultimo_login_dias": 95},
    {"id": 6, "nome": "Patricia Costa", "nivel_acesso": "usuario", "ultimo_login_dias": 200},
]


# =========================================================
# SEU CÓDIGO VAI AQUI

# 1. Defina a função 'analisar_perfis_de_usuario' que recebe uma lista.
def analisar_perfis_de_usuario(lista):
    total_admins = 0
    total_inativos = 0

    #    ... sua lógica com for e if vai aqui dentro ...
    for usuario in lista:
        if usuario["nivel_acesso"] == "admin":
            total_admins += 1
        if usuario["ultimo_login_dias"] > 90:
            total_inativos += 1

    #    ... não se esqueça do 'return' no final ...
    return total_admins, total_inativos

# 2. Chame a sua função, passando a 'lista_de_usuarios' para ela.
#    Guarde os dois valores que ela retorna em duas variáveis.
total_user, total_inactive = analisar_perfis_de_usuario(lista_de_usuarios)

# =========================================================


# 3. Imprima o resultado (esta parte já está pronta para quando seu código funcionar)
print("--- Relatório de Segurança de Contas ---")
print(f"Contas com privilégio de Administrador: {total_user}")
print(f"Contas consideradas inativas (> 90 dias): {total_inactive}")