"""
init_db.py — Inicializa o banco de dados.
Execute uma vez antes de rodar o servidor: python init_db.py
"""
import sqlite3

BANCO = "database.db"

def criar_tabelas():
    conn = sqlite3.connect(BANCO)
    c = conn.cursor()

    # Tabela de usuários
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            nome          TEXT    NOT NULL,
            email         TEXT    NOT NULL UNIQUE,
            senha_hash    TEXT    NOT NULL,
            data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabela de denúncias (com FK para usuario)
    c.execute("""
        CREATE TABLE IF NOT EXISTS denuncias (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            endereco         TEXT    NOT NULL,
            cep              TEXT,
            ponto_referencia TEXT,
            tipo             TEXT    NOT NULL,
            descricao        TEXT,
            status           TEXT    NOT NULL DEFAULT 'aberta',
            latitude         REAL,
            longitude        REAL,
            data             DATETIME DEFAULT CURRENT_TIMESTAMP,
            usuario_id       INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        )
    """)

    # Adiciona coluna usuario_id em bancos já existentes sem ela
    try:
        c.execute("ALTER TABLE denuncias ADD COLUMN usuario_id INTEGER")
    except Exception:
        pass  # coluna já existe

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
