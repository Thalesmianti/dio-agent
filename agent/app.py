import sqlite3


def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    try:
        cursor = conexao.execute(
            "SELECT 1 FROM usuarios WHERE username = ? AND password = ? LIMIT 1",
            (usuario, senha),
        )
        resultado = cursor.fetchone()
    finally:
        conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."