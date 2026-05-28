"""
denuncia_model.py — Model
Responsabilidade: executar os comandos SQL no banco de dados.
Não sabe nada sobre HTTP, validação ou regras de negócio.
"""

from .db import get_db


def db_listar():
    """Retorna todas as denúncias ordenadas pela mais recente."""
    db = get_db()
    rows = db.execute("SELECT * FROM denuncias ORDER BY data DESC").fetchall()
    return [dict(r) for r in rows]


def db_buscar_por_id(id):
    """Retorna uma denúncia pelo id, ou None se não existir."""
    db = get_db()
    row = db.execute("SELECT * FROM denuncias WHERE id = ?", (id,)).fetchone()
    return dict(row) if row else None


def db_criar(dados):
    """Insere uma nova denúncia no banco e retorna o id gerado."""
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO denuncias (endereco, cep, ponto_referencia, tipo, descricao, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            dados["endereco"],
            dados.get("cep"),
            dados.get("ponto_referencia"),
            dados["tipo"],
            dados.get("descricao"),
            dados.get("latitude"),
            dados.get("longitude"),
        ),
    )
    db.commit()
    return cursor.lastrowid  # id gerado automaticamente pelo banco


def db_atualizar(id, campos):
    """Atualiza apenas os campos recebidos na denúncia de determinado id."""
    db = get_db()

    # Monta o SET dinamicamente com apenas os campos enviados
    # ex: campos = {"status": "concluida"} → "status = ?"
    set_sql = ", ".join(f"{k} = ?" for k in campos)
    valores = list(campos.values()) + [id]

    db.execute(f"UPDATE denuncias SET {set_sql} WHERE id = ?", valores)
    db.commit()


def db_excluir(id):
    """Remove a denúncia de determinado id do banco."""
    db = get_db()
    db.execute("DELETE FROM denuncias WHERE id = ?", (id,))
    db.commit()
