"""
auth_service.py — Service de autenticação.
Responsabilidade: validações e regras de negócio de login e registro.
Usa werkzeug para hash seguro de senhas (nunca salvar senha em texto puro).
"""
from werkzeug.security import generate_password_hash, check_password_hash
from .usuario_model import db_criar_usuario, db_buscar_por_email, db_buscar_por_id


def servico_registrar(nome, email, senha):
    """
    Valida os dados e cria um novo usuário.
    Retorna o id criado, ou levanta ValueError se os dados forem inválidos.
    """
    nome  = (nome  or "").strip()
    email = (email or "").strip().lower()
    senha = (senha or "").strip()

    if not nome:
        raise ValueError("O nome é obrigatório.")
    if not email or "@" not in email:
        raise ValueError("E-mail inválido.")
    if len(senha) < 6:
        raise ValueError("A senha deve ter pelo menos 6 caracteres.")
    if db_buscar_por_email(email):
        raise ValueError("Este e-mail já está cadastrado.")

    # generate_password_hash cria um hash seguro — nunca salvar senha em texto puro
    senha_hash = generate_password_hash(senha)
    return db_criar_usuario(nome, email, senha_hash)


def servico_login(email, senha):
    """
    Valida as credenciais.
    Retorna o dicionário do usuário se correto, ou levanta ValueError.
    """
    email = (email or "").strip().lower()
    senha = (senha or "").strip()

    usuario = db_buscar_por_email(email)

    # check_password_hash compara a senha com o hash salvo no banco
    if not usuario or not check_password_hash(usuario["senha_hash"], senha):
        raise ValueError("E-mail ou senha incorretos.")

    return usuario


def servico_buscar_usuario(id):
    """Retorna os dados públicos do usuário (sem o hash da senha)."""
    usuario = db_buscar_por_id(id)
    if not usuario:
        raise ValueError("Usuário não encontrado.")

    # Remove o hash da senha antes de devolver ao frontend
    usuario.pop("senha_hash", None)
    return usuario
