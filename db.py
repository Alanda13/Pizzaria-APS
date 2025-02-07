import sqlite3
from flask import g

DATABASE = 'pizzaria.db'

def get_db():
    """Conecta-se ao banco de dados SQLite"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    """Cria as tabelas no banco de dados"""
    from app import app  # Importa a instância do Flask
    with app.app_context():  # Cria o contexto da aplicação
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def close_db(e=None):
    """Fecha a conexão com o banco de dados"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
