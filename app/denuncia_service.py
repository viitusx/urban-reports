"""
denuncia_service.py — Service de denúncias.
Responsabilidade: validações e regras de negócio.
"""
from .denuncia_model import db_listar, db_buscar_por_id, db_criar, db_atualizar, db_excluir

STATUS_VALIDOS = {"aberta", "em_ajuste", "concluida", "nao_houve"}
TIPOS_VALIDOS  = {"buraco", "fiacao_solta", "alagamento", "outros"}


def servico_listar(usuario_id):
    return db_listar(usuario_id)


def servico_criar(dados, usuario_id):
    endereco = (dados.get("endereco") or "").strip()
    tipo     = (dados.get("tipo") or "").strip()

    if not endereco:
        raise ValueError("O campo 'endereço' é obrigatório.")
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo inválido. Use: {', '.join(TIPOS_VALIDOS)}")

    dados_limpos = {
        "endereco":         endereco,
        "cep":              dados.get("cep"),
        "ponto_referencia": dados.get("ponto_referencia"),
        "tipo":             tipo,
        "descricao":        dados.get("descricao"),
        "latitude":         dados.get("latitude"),
        "longitude":        dados.get("longitude"),
    }
    return db_criar(dados_limpos, usuario_id)


def servico_atualizar(id, dados, usuario_id):
    denuncia = db_buscar_por_id(id)
    if not denuncia:
        raise ValueError("Denúncia não encontrada.")

    # Garante que o usuário só edita suas próprias denúncias
    if denuncia.get("usuario_id") != usuario_id:
        raise PermissionError("Sem permissão para editar esta denúncia.")

    campos = {}
    if dados.get("endereco", "").strip():
        campos["endereco"] = dados["endereco"].strip()
    if "cep" in dados:
        campos["cep"] = dados["cep"]
    if "ponto_referencia" in dados:
        campos["ponto_referencia"] = dados["ponto_referencia"]
    if dados.get("tipo") in TIPOS_VALIDOS:
        campos["tipo"] = dados["tipo"]
    if "descricao" in dados:
        campos["descricao"] = dados["descricao"]
    if dados.get("status") in STATUS_VALIDOS:
        campos["status"] = dados["status"]
    if "latitude" in dados:
        campos["latitude"] = dados["latitude"]
    if "longitude" in dados:
        campos["longitude"] = dados["longitude"]

    if not campos:
        raise ValueError("Nenhum campo válido para atualizar.")

    db_atualizar(id, campos)


def servico_excluir(id, usuario_id):
    denuncia = db_buscar_por_id(id)
    if not denuncia:
        raise ValueError("Denúncia não encontrada.")

    # Garante que o usuário só exclui suas próprias denúncias
    if denuncia.get("usuario_id") != usuario_id:
        raise PermissionError("Sem permissão para excluir esta denúncia.")

    db_excluir(id)
