# session_11.py

# Pode copiar esta lista
lista_de_ativos = [
    {"id": 101, "nome": "Servidor de Aplicação Alpha", "status": "ativo"},
    {"id": 102, "nome": "Notebook Engenharia 15", "status": "ativo"},
    {"id": 203, "nome": "Storage NAS Principal", "status": "inativo"},
    {"id": 404, "nome": "Roteador de Borda", "status": "manutenção"},
    {"id": 500, "nome": "Servidor de Banco de Dados", "status": "ativo"},
]

def encontrar_ativo_na_lista(lista, id_procurado):
    """
    (O(n)) Percorre uma lista de dicionários para encontrar um ativo pelo ID.
    Retorna o dicionário do ativo ou None se não encontrar.
    """
    for ativo in lista:
        if ativo["id"] == id_procurado:
            return ativo
    return None

def criar_dicionario_de_ativos(lista):
    """
    (O(n)) Recebe uma lista de ativos e retorna um dicionário otimizado
    para busca, onde a chave é o ID do ativo.
    """
    dicionario_de_ativos = {}
    for ativo in lista:
        id_do_ativo = ativo["id"]
        dicionario_de_ativos[id_do_ativo] = ativo
    return dicionario_de_ativos

# =========================================================
if __name__ == "__main__":
    
    id_a_buscar = 404
    
    print(f"--- Buscando o ativo com ID {id_a_buscar} ---")

    # 1. Teste da Forma Lenta (O(n))
    print("\nExecutando busca linear na lista...")
    ativo_encontrado_lista = encontrar_ativo_na_lista(lista_de_ativos, id_a_buscar)
    if ativo_encontrado_lista:
        print(f"-> Resultado da busca na lista: {ativo_encontrado_lista}")
    else:
        print(f"-> Ativo com ID {id_a_buscar} não encontrado na lista.")
    
    print("\n" + "="*40 + "\n")

    # 2. Preparação e Teste da Forma Rápida (O(1))
    print("Criando índice de ativos (dicionário) para otimizar buscas...")
    inventario_otimizado = criar_dicionario_de_ativos(lista_de_ativos)
    
    print(f"Buscando ativo com ID {id_a_buscar} no dicionário...")
    # A busca aqui é direta, sem laço 'for'!
    if id_a_buscar in inventario_otimizado:
        ativo_encontrado_dict = inventario_otimizado[id_a_buscar]
        print(f"-> Resultado da busca no dicionário: {ativo_encontrado_dict}")
    else:
        print(f"-> Ativo com ID {id_a_buscar} não encontrado no dicionário.")


    # 3. Responda as perguntas de reflexão aqui em comentários:
    # Pergunta 1: Qual o Big O da função encontrar_ativo_na_lista?
    # Resposta 1: O Big O desta função é O(n), pois no pior caso ela precisa percorrer todos os 'n' elementos da lista.
    
    # Pergunta 2: Qual o Big O da busca direta no dicionário `inventario_otimizado[id_a_buscar]`?
    # Resposta 2:O Big O desta operação é O(1), pois o acesso a um valor em um dicionário por chave é feito em tempo constante.
    
    # Pergunta 3: Em que cenário valeria a pena pagar o custo de rodar a função `criar_dicionario_de_ativos` (que tem custo O(n)) para obter buscas mais rápidas depois?
    # Resposta 3: Valeria a pena quando temos muitas buscas a serem feitas após a criação do dicionário, especialmente se o número de buscas for significativamente maior que o número de ativos. Nesse caso, o custo inicial de O(n) para criar o dicionário é compensado pelo ganho de eficiência nas buscas subsequentes, que são O(1).
# =========================================================