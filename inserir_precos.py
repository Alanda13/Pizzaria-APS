import sqlite3

# Conectar ao banco de dados SQLite (agora no caminho correto)
conn = sqlite3.connect('pizzaria.db')  # Caminho correto para o banco de dados na raiz

# Criação do cursor para executar comandos no banco
cursor = conn.cursor()

# Preços das pizzas (exemplo de dados)
pizzas = [
    ('Mussarela', 'Média', 30.00),
    ('Mussarela', 'Grande', 40.00),
    ('Mussarela', 'Gigante', 50.00),
    ('Calabresa', 'Média', 32.00),
    ('Calabresa', 'Grande', 42.00),
    ('Calabresa', 'Gigante', 55.00),
    ('Frango', 'Média', 28.00),
    ('Frango', 'Grande', 38.00),
    ('Frango', 'Gigante', 48.00)
]

# Inserir os preços na tabela 'pizzas'
cursor.executemany('INSERT INTO pizzas (sabor, tamanho, preco) VALUES (?, ?, ?)', pizzas)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
conn.close()

print("Preços inseridos com sucesso!")
