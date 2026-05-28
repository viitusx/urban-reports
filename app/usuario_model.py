"""
usuario_model.py — Model de usuário.
Responsabilidade: operações SQL da tabela usuario.
"""
from .db import get_db


def db_criar_usuario(nome, email, senha_hash):
    """Insere um novo usuário e retorna o id gerado."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO usuario (nome, email, senha_hash) VALUES (?, ?, ?)",
        (nome, email, senha_hash),
    )
    db.commit()
    return cursor.lastrowid


def db_buscar_por_email(email):
    """Retorna o usuário com o email fornecido, ou None."""
    db = get_db()
    row = db.execute("SELECT * FROM usuario WHERE email = ?", (email,)).fetchone()
    return dict(row) if row else None


def db_buscar_por_id(id):
    """Retorna o usuário com o id fornecido, ou None."""
    db = get_db()
    row = db.execute("SELECT * FROM usuario WHERE id = ?", (id,)).fetchone()
    return dict(row) if row else None
