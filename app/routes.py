"""
routes.py — Controller de denúncias.
Responsabilidade: receber requisições HTTP e devolver respostas JSON.
Todas as rotas exigem que o usuário esteja autenticado.
"""
from flask import Blueprint, request, jsonify, session
from .denuncia_service import servico_listar, servico_criar, servico_atualizar, servico_excluir

bp = Blueprint("denuncias", __name__)


def usuario_logado():
    """Retorna o id do usuário na sessão, ou None se não estiver logado."""
    return session.get("usuario_id")


@bp.route("/denuncias", methods=["GET"])
def listar():
    uid = usuario_logado()
    if not uid:
        return jsonify({"erro": "Não autenticado."}), 401

    return jsonify(servico_listar(uid))


@bp.route("/denuncias", methods=["POST"])
def criar():
    uid = usuario_logado()
    if not uid:
        return jsonify({"erro": "Não autenticado."}), 401

    try:
        id_criado = servico_criar(request.get_json(), uid)
        return jsonify({"mensagem": "Denúncia criada!", "id": id_criado}), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@bp.route("/denuncias/<int:id>", methods=["PUT"])
def atualizar(id):
    uid = usuario_logado()
    if not uid:
        return jsonify({"erro": "Não autenticado."}), 401

    try:
        servico_atualizar(id, request.get_json(), uid)
        return jsonify({"mensagem": "Denúncia atualizada!"})
    except PermissionError as e:
        return jsonify({"erro": str(e)}), 403
    except ValueError as e:
        status = 404 if "não encontrada" in str(e) else 400
        return jsonify({"erro": str(e)}), status


@bp.route("/denuncias/<int:id>", methods=["DELETE"])
def excluir(id):
    uid = usuario_logado()
    if not uid:
        return jsonify({"erro": "Não autenticado."}), 401

    try:
        servico_excluir(id, uid)
        return jsonify({"mensagem": "Denúncia excluída!"})
    except PermissionError as e:
        return jsonify({"erro": str(e)}), 403
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
