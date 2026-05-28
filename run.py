"""
run.py — Ponto de entrada do servidor Flask.
Execute com: python run.py
"""

from app import criar_app

app = criar_app()  # factory function: configura extensões, blueprints e settings antes de retornar a instância

if __name__ == "__main__":
    app.run(debug=True)