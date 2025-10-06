import csv

import utils

print(f"Executando o código de main.py. O valor de __name__ é: '{__name__}'")

if __name__ == "__main__":

    usuarios_do_arquivo = []

    # 4. Abrimos o arquivo CSV para leitura
    with open('usuarios.csv', mode='r', encoding='utf-8') as arquivo_csv:
        # O DictReader lê cada linha do CSV como um dicionário
        leitor_csv = csv.DictReader(arquivo_csv)

        # Fazemos um laço 'for' para ler cada linha do arquivo'
        for linha in leitor_csv:
            usuarios_do_arquivo.append(linha)

    # 5.Agora, passamos a lista que lemos do arquivo para a nossa função
    admins, inativos = utils.analisar_perfis_de_usuario(usuarios_do_arquivo)

    # 6. Imprimimos o resultado na tela para verificar
    print("--- Análise Concluída (lido do arquivo CSV) ---")
    print(f"Total de Administradores: {admins}")
    print(f"Total de Usuários Inativos: {inativos}")

    # 7. Salvando o resultado em um novo arquivo
    with open('relatorio.txt', mode='w', encoding='utf-8') as arquivo_relatorio:
        arquivo_relatorio.write("--- Relatório de Segurança de Contas ---\n")
        arquivo_relatorio.write(f"Contas com privilégio de Administrador: {admins}\n")
        arquivo_relatorio.write(f"Contas consideradas inativas (> 90 dias): {inativos}\n")        arquivo_relatorio.write(f"Contas consideradas inativas (> 90 dias): {inativos}\n")        arquivo_relatorio.write(f"Contas consideradas inativas (> 90 dias): {inativos}\n")