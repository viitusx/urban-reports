"""
auth_routes.py — Controller de autenticação.
Responsabilidade: receber requisições HTTP de login/registro e gerenciar sessão.
"""
from flask import Blueprint, request, jsonify, session
from .auth_service import servico_registrar, servico_login, servico_buscar_usuario

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/registro", methods=["POST"])
def registro():
    dados = request.get_json()
    try:
        id_usuario = servico_registrar(
            dados.get("nome"),
            dados.get("email"),
            dados.get("senha"),
        )
        # Inicia a sessão automaticamente após o registro
        session["usuario_id"] = id_usuario
        return jsonify({"mensagem": "Conta criada com sucesso!"}), 201

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    try:
        usuario = servico_login(dados.get("email"), dados.get("senha"))

        # session é um dicionário especial do Flask — os dados ficam
        # num cookie assinado no navegador do usuário
        session["usuario_id"] = usuario["id"]
        return jsonify({"mensagem": "Login realizado com sucesso!"})

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()  # apaga todos os dados da sessão
    return jsonify({"mensagem": "Logout realizado."})


@auth_bp.route("/me", methods=["GET"])
def me():
    """Retorna os dados do usuário logado. Usado pelo frontend para verificar autenticação."""
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        return jsonify({"erro": "Não autenticado."}), 401

    try:
        usuario = servico_buscar_usuario(usuario_id)
        return jsonify(usuario)
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 404
