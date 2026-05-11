from app.db import get_db

def criar_denuncia(dados):
    conn = get_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO denuncias 
    (titulo, descricao, status, usuario_id, categoria_id, latitude, longitude, endereco)
    VALUES (%s, %s, 'aberta', %s, %s, %s, %s, %s)
    """

    values = (
        dados['titulo'],
        dados['descricao'],
        dados['usuario_id'],
        dados['categoria_id'],
        dados['latitude'],
        dados['longitude'],
        dados['endereco']
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()


def listar_denuncias():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM denuncias")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result