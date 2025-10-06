# Sessão 6.2

class AtivoTI:
    def __init__(self, id_ativo, responsavel, status="ativo"):
        self.id_ativo = id_ativo
        self.responsavel = responsavel
        self.status = status
        # Atributo "protegido" com um underline (veremos no encapsulamento)
        self._numero_de_serie = "ABC123XYZ"

    def verificar_saude(self):
        print(f"Verificando saúde do ativo {self.id_ativo}... Status: {self.status}")

    def exibir_info(self):
        print(f"ID: {self.id_ativo}, Responsável: {self.responsavel}, Status: {self.status}")

class Servidor(AtivoTI):
    def __init__(self, id_ativo, responsavel, rack_unit, status="ativo"):
        # 'super().__init__(...)' chama o construtor da classe pai (AtivoTI)
        super().__init__(id_ativo, responsavel, status)

        #Este é um atributo especifico da classe Servidor
        self.rack_unit = rack_unit

    def verificar_saude(self):
        print(f"Verificando saúde do servidor {self.id_ativo}: pingando IP, checando CPU...")



class Notebook(AtivoTI):
    def __init__(self, id_ativo, responsavel, tamanho_tela, status="ativo"):
        super().__init__(id_ativo, responsavel, status)

        # Atritubo especifico da classe Notebook
        self.tamanho_tela = tamanho_tela
    
    def verificar_saude(self):
        print(f"Verificando saúde do notebook {self.id_ativo}: Checando Nível da bateria...")

class Roteador(AtivoTI):
    def __init__(self, id_ativo, responsavel, numero_portas, status="ativo"):
        super().__init__(id_ativo, responsavel, status)
        self.numero_portas = numero_portas

    def verificar_saude(self):
        print(f"Verificando saúde do roteador {self.id_ativo}: Checando conexões de rede, verificando tráfego...")

# O código abaixo fica no escopo principal, após as definições das classes
if __name__ == "__main__":
    
    # Criando instâncias de diferentes classes
    servidor_web = Servidor(id_ativo="SRV-01", responsavel="Equipe Infra", rack_unit=2)
    notebook_dev = Notebook(id_ativo="NTB-DEV-15", responsavel="Mariana", tamanho_tela=14)
    ativo_generico = AtivoTI(id_ativo="GEN-01", responsavel="Carlos")
    roteador = Roteador(id_ativo="RTR-EDGE-1", responsavel="Administradores de Rede", numero_portas=16)

    #Criando uma lista com objetos de tipos diferentes
    inventario = [servidor_web, notebook_dev, ativo_generico, roteador]

    print("--- Relatório de Verificação de Saúde ---")

    # A MÁGICA DO POLIMORFISMO ACONTECE AQUI!
    # O laço não se importa com o tipo de objeto (Servidor, Notebook ou AtivoTI).
    # Ele apenas chama o método 'verificar_saude()', e cada objeto sabe como
    #executar a sua própria versão do método.
    for ativo in inventario:
        ativo.verificar_saude()


