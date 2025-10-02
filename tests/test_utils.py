from utils import analisar_perfis_de_usuario


def test_analisar_perfis_de_usuario():
    usuarios_teste = [
        {"nome": "Alice", "nivel_acesso": "admin", "ultimo_login_dias": "10"},
        {"nome": "Bob", "nivel_acesso": "user", "ultimo_login_dias": "95"},
        {"nome": "Charlie", "nivel_acesso": "admin", "ultimo_login_dias": "120"},
        {"nome": "David", "nivel_acesso": "user", "ultimo_login_dias": "30"},
        {"nome": "Eve", "nivel_acesso": "user", "ultimo_login_dias": "200"},
    ]

    admins, inativos = analisar_perfis_de_usuario(usuarios_teste)
    assert admins == 2, f"Esperado 2 admins, mas obteve {admins}"
    assert inativos == 3, f"Esperado 3 usuários inativos, mas obteve {inativos}"

def test_analisar_perfis_de_usuario2():
    usuarios_teste2 = []

    admins2, inativos2 = analisar_perfis_de_usuario(usuarios_teste2)
    assert (admins2, inativos2) == (0, 0), f"Esperado (0, 0) para lista vazia, mas obteve ({admins2}, {inativos2})"