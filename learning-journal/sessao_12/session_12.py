class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None #Filho da esquerda
        self.direita = None #Filho da direita

class BinarySearchTree:
    def __init__(self):
        self.raiz = None # A árvore começa vazia, sem raiz

    def insert(self, valor):
        """Método público para inserir um novo valor na árvore."""
        if self.raiz is None:
            self.raiz = TreeNode(valor)
        else:
            self._insert_recursivo(self.raiz, valor)
    
    def _insert_recursivo(self, no_atual, valor):
        """(SUA TAREFA) Método auxiliar para encontrar onde inserir o novo nó."""
        # Pense na lógica como uma série de perguntas:
        # 1. O 'valor' que quero inserir é MENOR que o valor do 'no_atual'?
        #    - Se sim, preciso olhar para a ESQUERDA.
        #    - A 'porta' da esquerda (no_atual.esquerda) está vazia (is None)?
        #        - Se sim, achei o lugar! Crie o TreeNode aqui.
        #        - Se não, delegue a tarefa para o filho da esquerda (recursão!).
        # 2. O 'valor' que quero inserir é MAIOR que o valor do 'no_atual'?
        #    - Se sim, o processo é o mesmo, mas para a DIREITA.
        # (Obs: não vamos inserir valores duplicados por enquanto)
        
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = TreeNode(valor)
            else:
                self._insert_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = TreeNode(valor)
            else:
                self._insert_recursivo(no_atual.direita, valor)
    
    def search(self, valor):
        """Método público para buscar um valor na árvore."""
        return self._search_recursivo(self.raiz, valor)
    
    def _search_recursivo(self, no_atual, valor):
        """(SUA TAREFA) Método auxiliar para buscar um valor recursivamente."""
        # Pense nos casos para parar a busca (casos base):
        # 1. Se o 'no_atual' é None, significa que chegamos a um galho sem saída.
        #    O valor não existe na árvore.
        # 2. Se o 'valor' do 'no_atual' é o que procuramos, encontramos!
        
        # Se não paramos, precisamos decidir para onde ir (passo recursivo):
        # 3. Se o 'valor' que buscamos é MENOR que o do 'no_atual', continue a
        #    busca pela sub-árvore da ESQUERDA.
        # 4. Se for MAIOR, continue a busca pela sub-árvore da DIREITA.
        if no_atual is None:
            return False
        if no_atual.valor == valor:
            return True
        elif valor < no_atual.valor:
            return self._search_recursivo(no_atual.esquerda, valor)
        else:
            return self._search_recursivo(no_atual.direita, valor)

#================================================================================

if __name__ == "__main__":
    bst = BinarySearchTree()
    print("Inserindo valores na Árvore Binária de Busca...")

    valores = [8, 3, 10, 1, 6, 14, 4, 7]
    for val in valores:
        bst.insert(val)
    
    print("Árvore construída).")

# Testando a busca
print("\n--- Testes de Busca ---")
print(f"Buscando pelo valor 6: {bst.search(6)}")   # Esperado: True
print(f"Buscando pelo valor 14: {bst.search(14)}") # Esperado: True
print(f"Buscando pelo valor 5: {bst.search(5)}")   # Esperado: False
print(f"Buscando pelo valor 11: {bst.search(11)}") # Esperado: False
