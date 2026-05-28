"""
routes.py — Controller
Responsabilidade: receber requisições HTTP e devolver respostas JSON.
Não contém regras de negócio nem SQL.
Delega toda a lógica para o Service.
"""

from flask import Blueprint, request, jsonify
from .denuncia_service import servico_listar, servico_criar, servico_atualizar, servico_excluir

bp = Blueprint("denuncias", __name__)


@bp.route("/denuncias", methods=["GET"])
def listar():
    denuncias = servico_listar()
    return jsonify(denuncias)


@bp.route("/denuncias", methods=["POST"])
def criar():
    try:
        id_criado = servico_criar(request.get_json())
        return jsonify({"mensagem": "Denúncia criada!", "id": id_criado}), 201

    except ValueError as erro:
        # ValueError vem do Service quando os dados são inválidos
        return jsonify({"erro": str(erro)}), 400


@bp.route("/denuncias/<int:id>", methods=["PUT"])
def atualizar(id):
    try:
        servico_atualizar(id, request.get_json())
        return jsonify({"mensagem": "Denúncia atualizada!"})

    except ValueError as erro:
        status = 404 if "não encontrada" in str(erro) else 400
        return jsonify({"erro": str(erro)}), status


@bp.route("/denuncias/<int:id>", methods=["DELETE"])
def excluir(id):
    try:
        servico_excluir(id)
        return jsonify({"mensagem": "Denúncia excluída!"})

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 404