from flask import Blueprint, request, jsonify
from app.db import get_db

bp = Blueprint("routes", __name__)

#  LISTAR DENÚNCIAS (se já não tiver)
@bp.route("/denuncias/", methods=["GET"])
def listar_denuncias():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM denuncias")
    dados = cursor.fetchall()

    denuncias = [dict(row) for row in dados]
    return jsonify(denuncias)


#  CRIAR DENÚNCIA
@bp.route("/denuncias/", methods=["POST"])
def criar_denuncia():
    data = request.get_json()

    titulo = data.get("titulo")
    descricao = data.get("descricao")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    # ✅ validação básica
    if not titulo:
        return jsonify({"erro": "Título é obrigatório"}), 400

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO denuncias (titulo, descricao, latitude, longitude)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, latitude, longitude))

    db.commit()

    return jsonify({
        "mensagem": "Denúncia criada com sucesso!"
    }), 201