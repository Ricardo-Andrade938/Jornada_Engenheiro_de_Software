inventario_de_ativo = [
    {"id": 1, "nome do ativo": "Notebook Dell Inspirion"},
    {"id": 2, "nome do ativo": "Notebook HP G7"},
    {"id": 3, "nome do ativo": "Workstation Lenovo"},
    {"id": 4, "nome do ativo": "Servidor HP proliant"},
    {"id": 5, "nome do ativo": "Desktop Positivo I9"},
    {"id": 6, "nome do ativo": "Macbook"},
]


class AdicionarAtivo:
    def __init__(self, inventario):
        self.inventario = inventario
    
    def adicionar_ativo(self, id, nome_do_ativo):
        novo_ativo = {"id": id, "nome do ativo": nome_do_ativo}
        self.inventario.append(novo_ativo)
        print(f"ativo {nome_do_ativo} adicionado com sucesso!")

    def adicionar_ativo2(self, id, nome_do_ativo2):
        novo_ativo2 = {"id": id, "nome do ativo2": nome_do_ativo2}
        self.inventario.insert(0, novo_ativo2)
        print(f"ativo {nome_do_ativo2} adicionado com sucesso!")

class ConsultarAtivo:
    def __init__(self, inventario):
        self.inventario = inventario

    def consultar_ativo(self, id):
        for ativo in self.inventario:
            if ativo["id"] == id:
                print(f"Ativo encontrado: {ativo}")

if __name__ == "__main__":
    gerenciado = input("Você deseja adicionar ou consultar um ativo? (adicionar com append/adicionar com insert/consultar): ").strip().lower()
    gerenciador = None
    if gerenciado == "adicionar com append":
        gerenciado = AdicionarAtivo(inventario_de_ativo)
        id = int(input("Digite o ID do ativo: "))
        nome_do_ativo = input("Digite o nome do ativo: ")
        if id in [ativo["id"] for ativo in inventario_de_ativo]:
            print("ID já existe. Por favor, escolha um ID único.")
        else:
            gerenciado.adicionar_ativo(id, nome_do_ativo)
    elif gerenciado == "adicionar com insert":
        gerenciado = AdicionarAtivo(inventario_de_ativo)
        id = int(input("Digite o ID do ativo: "))
        nome_do_ativo2 = input("Digite o nome do ativo: ")
        if id in [ativo["id"] for ativo in inventario_de_ativo]:
            print("ID já existe. Por favor, escolha um ID único.")
        else:
            gerenciado.adicionar_ativo2(id, nome_do_ativo2)
    elif gerenciado == "consultar":
        gerenciado = ConsultarAtivo(inventario_de_ativo)
        id = int(input("Digite o ID do ativo que deseja consultar: "))
        gerenciado.consultar_ativo(id)
    else:
        print("Opção inválida. Por favor, escolha 'adicionar' ou 'consultar'.")

print("\nFim do programa.")