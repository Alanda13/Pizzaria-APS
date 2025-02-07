from app import app
from db import init_db

# Inicializa o banco de dados com o contexto da aplicação
with app.app_context():
    init_db()
