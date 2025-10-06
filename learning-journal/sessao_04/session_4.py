# 1. Importamos o módulo 'csv' para nos ajudar a ler o arquivo
import csv

# 2. Copie a função que você criou na Sessão 3 para cá

def analisar_perfis_de_usuario(lista):
    total_admins = 0
    total_inativos = 0

    #    ... sua lógica com for e if vai aqui dentro ...
    for usuario in lista:
        if usuario["nivel_acesso"] == "admin":
            total_admins += 1
        if int(usuario["ultimo_login_dias"]) > 90:
            total_inativos += 1

    #    ... não se esqueça do 'return' no final ...
    return total_admins, total_inativos

# 3 Criamos uma lista vazia para guardar os usuários que vamos ler do arquivo
usuarios_do_arquivo = []

# 4. Abrimos o arquivo CSV para leitura
with open('usuarios.csv', mode='r', encoding='utf-8') as arquivo_csv:
    # O DictReader lê cada linha do CSV como um dicionário
    leitor_csv = csv.DictReader(arquivo_csv)

    # Fazemos um laço 'for' para ler cada linha do arquivo'
    for linha in leitor_csv:
        usuarios_do_arquivo.append(linha)

# 5.Agora, passamos a lista que lemos do arquivo para a nossa função
admins, inativos = analisar_perfis_de_usuario(usuarios_do_arquivo)

# 6. Imprimimos o resultado na tela para verificar
print("--- Análise Concluída (lido do arquivo CSV) ---")
print(f"Total de Administradores: {admins}")
print(f"Total de Usuários Inativos: {inativos}")

# 7. Salvando o resultado em um novo arquivo
with open('relatorio.txt', mode='w', encoding='utf-8') as arquivo_relatorio:
    arquivo_relatorio.write("--- Relatório de Segurança de Contas ---\n")
    arquivo_relatorio.write(f"Contas com privilégio de Administrador: {admins}\n")
    arquivo_relatorio.write(f"Contas consideradas inativas (> 90 dias): {inativos}\n")