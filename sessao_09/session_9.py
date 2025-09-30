from collections import deque

fila_de_atendimento = deque()

class AcoesUser:
    def __init__(self):
        self.acoes = []

    def adicionarAcao(self, acao):
        self.acoes.append(acao)

    def listarAcao(self):
        print("Ações do usuário:")
        if not self.acoes:
            print(" Nenhuma ação registrada.")
        else:
            for acao in self.acoes:
                print(f" O usuário realizou as seguintes operações: {acao}")

if __name__ == "__main__":
    acao = input("Digite o que deseja fazer:").strip().lower()
    operacoes = AcoesUser()
    operacoes.adicionarAcao(acao)
    acao2 = input("Deseja realizar mais alguma coisa? Sim/Nao").strip().lower()
    while acao2 == "sim":
            acao = input("Digite o que deseja fazer:").strip().lower()
            operacoes.adicionarAcao(acao)
            acao2 = input("Deseja realizar mais alguma coisa? Sim/Nao").strip().lower()
            if acao2 == "nao":
                break
            print("Fim do programa.")
    
    operacoes.listarAcao()

    desfazer = input("Deseja desfazer a última ação? Sim/Nao").strip().lower()
    if desfazer == "sim":
        if operacoes.acoes:
            ultima_acao = operacoes.acoes.pop()
            print(f"A última ação '{ultima_acao}' foi desfeita.")
        else:
            print("Nenhuma ação para desfazer.")
    
    operacoes.listarAcao()


fila_de_atendimento.append("A01")
fila_de_atendimento.append("A02")
fila_de_atendimento.append("A03")

proximo_cliete = fila_de_atendimento.popleft()
print(f"Atendendo o cliente: {proximo_cliete}")
print(f"Fila atual: {list(fila_de_atendimento)}")
