"""
app/__init__.py — Fábrica da aplicação Flask.
"""
from flask import Flask
from flask_cors import CORS
from .routes import bp
from .auth_routes import auth_bp

def criar_app():
    app = Flask(__name__)

    # Chave secreta para assinar os cookies de sessão
    app.secret_key = "sdu-chave-secreta-2026"

    # supports_credentials=True permite que o navegador envie cookies nas requisições
    CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5500",
                                                   "http://localhost:5500",
                                                   "http://127.0.0.1:8080",
                                                   "null"])

    app.register_blueprint(bp)
    app.register_blueprint(auth_bp)

    return app
