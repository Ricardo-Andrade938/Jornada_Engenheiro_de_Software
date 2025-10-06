# session_10.py
 
# PASSO 1: A classe do Bloco de Construção (O "Vagão")
# Esta classe representa um único elemento na nossa lista.
class Node:
    def __init__(self, dado):
        self.dado = dado      # O dado que queremos armazenar (ex: "A", "B", 1, 2...)
        self.proximo = None   # O "ponteiro" para o próximo nó. Começa como None.
 
# PASSO 2: A classe Gerenciadora (A "Locomotiva")
# Esta classe vai gerenciar a cadeia de Nós.
class LinkedList:
    def __init__(self):
        # Uma lista vazia começa sem um primeiro nó.
        self.head = None
 
    def append(self, dado):
        """Adiciona um novo nó com o 'dado' fornecido ao FINAL da lista."""
        novo_no = Node(dado)
 
        # CASO DE BORDA: Se a lista estiver vazia (head is None),
        # o novo nó se torna o primeiro (o head).
        ultimo_no = self.head
        if self.head is None:
            self.head = novo_no
            return
        
        # Se a lista NÃO estiver vazia, precisamos percorrer até o final
        # e conectar o último nó ao novo_no.
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        
        ultimo_no.proximo = novo_no

    def prepend(self, dado):
        """Adiciona um novo nó com o 'dado' no INÍCIO da lista."""
        novo_no = Node(dado)
        novo_no.proximo = self.head
        self.head = novo_no
        return
    
    def delete(self, dado_a_remover):
        """Encontra e remove o primeiro nó que contém o 'dado_a_remover'."""
        no_atual = self.head
        no_anterior = None
        if self.head is None:
            return
        while no_atual and no_atual.dado != dado_a_remover:
            no_anterior = no_atual
            no_atual = no_atual.proximo
        if no_atual is None:
            return
        if no_anterior is None:
            self.head = no_atual.proximo
        else:
            no_anterior.proximo = no_atual.proximo
        return
            
            
    def display(self):
        """Exibe todos os dados da lista, do início ao fim."""
  # Crie uma lista temporária para guardar os dados
  # Comece a percorrer a partir do 'head'
        # Use um laço 'while' para continuar enquanto o nó atual não for None
        # Adicione o 'dado' de cada nó na lista temporária
        # Imprima a lista no final.
        dados = []
        no_atual = self.head
        while no_atual:
            dados.append(no_atual.dado)
            no_atual = no_atual.proximo
        print(dados)


# =========================================================
# CÓDIGO DE TESTE (para quando você implementar os métodos)
if __name__ == "__main__":

    # Criando nossa lista ligada
    minha_lista_de_jogos = LinkedList()

    # Testando o método append
    print("Adicionando jogos à lista de tarefas...")
    minha_lista_de_jogos.append("The Witcher 3")
    minha_lista_de_jogos.append("Cyberpunk 2077")
    minha_lista_de_jogos.append("Baldur's Gate 3")
 
    # Testando o método display
    print("\nMinha lista de jogos para zerar:")
    minha_lista_de_jogos.display() # Saída esperada: ['The Witcher 3', 'Cyberpunk 2077', "Baldur's Gate 3"]
 
    print("\nAdicionando mais um jogo...")
    minha_lista_de_jogos.append("Elden Ring")
    minha_lista_de_jogos.display() # Saída esperada: ['The Witcher 3', 'Cyberpunk 2077', "Baldur's Gate 3", 'Elden Ring']

    print("\nAdicionando 'Diablo IV' no início da lista...")
    minha_lista_de_jogos.prepend("Diablo IV")
    minha_lista_de_jogos.display()
    # Saída esperada: ['Diablo IV', 'The Witcher 3', 'Cyberpunk 2077', "Baldur's Gate 3", 'Elden Ring']    venv\Scripts\activate

    print("\nRemovendo 'Cyberpunk 2077' da lista...")
    minha_lista_de_jogos.delete("Cyberpunk 2077")
    minha_lista_de_jogos.display()
    # Saída esperada: ['Diablo IV', 'The Witcher 3', "Baldur's Gate 3", 'Elden Ring']

    print("\nTentando remover um jogo que não existe...")
    minha_lista_de_jogos.delete("Final Fantasy VII")
    minha_lista_de_jogos.display() # A lista deve continuar igual