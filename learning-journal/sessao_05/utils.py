print(f"Executando o código de utils.py. O valor de __name__ é: '{__name__}'")

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