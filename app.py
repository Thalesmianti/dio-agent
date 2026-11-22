import sqlite3

def inicializar_banco():
    """Cria a tabela de usuários e insere dados de teste em memória."""
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            senha TEXT
        )
    """)
    
    # Usuário de teste cadastrado no banco
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha_secreta_123')")
    conexao.commit()
    return conexao

def login_vulneravel(conexao, usuario, senha):
    """
    Exemplo VULNERÁVEL a SQL Injection:
    Concatena diretamente os dados do usuário na consulta SQL.
    """
    cursor = conexao.cursor()
    query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
    print(f"\n[QUERY EXECUTADA]: {query}")
    
    cursor.execute(query)
    resultado = cursor.fetchone()
    
    if resultado:
        print("✅ Login realizado com sucesso!")
        return True
    else:
        print("❌ Usuário ou senha inválidos.")
        return False

def login_seguro(conexao, usuario, senha):
    """
    Exemplo SEGURO usando Prepared Statements (consultas parametrizadas):
    Os dados são passados como tupla separada e nunca concatenados na query.
    """
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    print(f"\n[QUERY PARAMETRIZADA]: {query} com parâmetros: ({usuario}, [OCULTO])")
    
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    
    if resultado:
        print("✅ Login realizado com sucesso!")
        return True
    else:
        print("❌ Usuário ou senha inválidos.")
        return False

if __name__ == "__main__":
    banco = inicializar_banco()
    
    print("=" * 50)
    print("TESTE 1: Login legítimo com credenciais corretas")
    print("=" * 50)
    login_vulneravel(banco, "admin", "senha_secreta_123")
    
    print("\n" + "=" * 50)
    print("TESTE 2: Ataque de SQL Injection na função vulnerável")
    print("O atacante envia usuario = \"admin' --\" e uma senha qualquer")
    print("=" * 50)
    login_vulneravel(banco, "admin' --", "senha_errada")
    
    print("\n" + "=" * 50)
    print("TESTE 3: Mesma tentativa de ataque na função segura")
    print("=" * 50)
    login_seguro(banco, "admin' --", "senha_errada")
