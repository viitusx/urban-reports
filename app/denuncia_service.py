"""
denuncia_service.py — Service
Responsabilidade: regras de negócio e validações.
Não sabe nada sobre HTTP (sem request, sem jsonify, sem códigos 400/404).
Fala com o Model para acessar o banco.
"""

from .denuncia_model import db_listar, db_buscar_por_id, db_criar, db_atualizar, db_excluir

STATUS_VALIDOS = {"aberta", "em_ajuste", "concluida", "nao_houve"}
TIPOS_VALIDOS  = {"buraco", "fiacao_solta", "alagamento", "outros"}


def servico_listar():
    """Devolve a lista de todas as denúncias."""
    return db_listar()


def servico_criar(dados):
    """
    Valida os dados e cria uma nova denúncia.
    Retorna o id criado, ou levanta ValueError se os dados forem inválidos.
    """
    endereco = (dados.get("endereco") or "").strip()
    tipo     = (dados.get("tipo") or "").strip()

    if not endereco:
        raise ValueError("O campo 'endereço' é obrigatório.")

    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo inválido. Use: {', '.join(TIPOS_VALIDOS)}")

    # Dados limpos e validados, envia para o Model salvar
    dados_limpos = {
        "endereco":        endereco,
        "cep":             dados.get("cep"),
        "ponto_referencia":dados.get("ponto_referencia"),
        "tipo":            tipo,
        "descricao":       dados.get("descricao"),
        "latitude":        dados.get("latitude"),
        "longitude":       dados.get("longitude"),
    }

    return db_criar(dados_limpos)


def servico_atualizar(id, dados):
    """
    Valida e atualiza os campos de uma denúncia.
    Levanta ValueError se a denúncia não existir ou os dados forem inválidos.
    """
    if not db_buscar_por_id(id):
        raise ValueError("Denúncia não encontrada.")

    # Monta apenas os campos válidos que vieram na requisição
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


def servico_excluir(id):
    """
    Exclui uma denúncia pelo id.
    Levanta ValueError se a denúncia não existir.
    """
    if not db_buscar_por_id(id):
        raise ValueError("Denúncia não encontrada.")

    db_excluir(id)
