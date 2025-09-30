# Sessão 6

class AtivoTI:
    # Este é o metodo construtor. É ele que "monta" o objeto quando ele é criado.
    # Ele define os atrbutos que todo AtivoTI terá.
    def __init__(self, hostname, ip, status="ativo", responsavel=None):
        self.hostname = hostname
        self.ip = ip
        self.status = status
        self.responsavel = responsavel

    # Este é um metodo. É uma função que pertence a classe
    # Note que o primeiro argumento é sempre 'self'.
    def exibir_status(self):
        print(f"O status do ativo '{self.hostname}' (IP: {self.ip}) é: {self.status} e o responsável pelo equipamento é {self.responsavel}.")

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"O status do ativo '{self.hostname}' foi atualizado para: {self.status}")

# O código abaixo fica fora da classe, no escopo principal.

print("--- Gerenciamento de Inventário ---")

# Criando a primeira instância (objeto) da classe AtivoTI
ativo1 = AtivoTI(hostname="SRV-DB-01", ip="192.168.1.15", status="manutenção", responsavel="Coordenador de Segurança Empresarial")

# Criando a segunda instância, completamente independente da primeira
ativo2 = AtivoTI(hostname="WS-USER-22", ip="192.168.1.10", responsavel="Analista de Sistemas")

# Terceira instancia, com valores diferentes
ativo3 = AtivoTI(hostname="DELL-LATITUDE-5400", ip="172.18.0.1", status="Em curto", responsavel="Estagiário de TI")

# Acessando os atributos (os dados) de cada objeto
print(f"O hostname do primeiro ativo é: {ativo1.hostname}")
print(f"O IP do segundo do segundo ativo é: {ativo2.ip}")

# Chamando metodo atualizar status:
ativo1.atualizar_status("Reestruturado")

# Chamando os métodos (as ações) de cada objeto
ativo1.exibir_status()
ativo2.exibir_status()
ativo3.exibir_status()
