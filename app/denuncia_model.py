"""
denuncia_model.py — Model de denúncias.
Responsabilidade: executar os comandos SQL no banco de dados.
"""
from .db import get_db


def db_listar(usuario_id):
    """Retorna todas as denúncias do usuário logado."""
    db = get_db()
    rows = db.execute(
        "SELECT * FROM denuncias WHERE usuario_id = ? ORDER BY data DESC",
        (usuario_id,)
    ).fetchall()
    return [dict(r) for r in rows]


def db_buscar_por_id(id):
    """Retorna uma denúncia pelo id, ou None se não existir."""
    db = get_db()
    row = db.execute("SELECT * FROM denuncias WHERE id = ?", (id,)).fetchone()
    return dict(row) if row else None


def db_criar(dados, usuario_id):
    """Insere uma nova denúncia vinculada ao usuário logado."""
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO denuncias
            (endereco, cep, ponto_referencia, tipo, descricao, latitude, longitude, usuario_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            dados["endereco"],
            dados.get("cep"),
            dados.get("ponto_referencia"),
            dados["tipo"],
            dados.get("descricao"),
            dados.get("latitude"),
            dados.get("longitude"),
            usuario_id,
        ),
    )
    db.commit()
    return cursor.lastrowid


def db_atualizar(id, campos):
    """Atualiza apenas os campos recebidos da denúncia de determinado id."""
    db = get_db()
    set_sql = ", ".join(f"{k} = ?" for k in campos)
    valores = list(campos.values()) + [id]
    db.execute(f"UPDATE denuncias SET {set_sql} WHERE id = ?", valores)
    db.commit()


def db_excluir(id):
    """Remove a denúncia pelo id."""
    db = get_db()
    db.execute("DELETE FROM denuncias WHERE id = ?", (id,))
    db.commit()
