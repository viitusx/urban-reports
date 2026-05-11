from flask import request, jsonify
from app.models.denuncia_model import criar_denuncia, listar_denuncias

def criar():
    dados = request.json

    if not dados.get('titulo') or not dados.get('latitude'):
        return jsonify({'erro': 'Dados obrigatórios faltando'}), 400

    criar_denuncia(dados)
    return jsonify({'mensagem': 'Denúncia criada com sucesso'}), 201


def listar():
    denuncias = listar_denuncias()
    return jsonify(denuncias)