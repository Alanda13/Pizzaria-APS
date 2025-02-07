import sqlite3

def test_query():
    # Conecta ao banco de dados
    conn = sqlite3.connect('pizzaria.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("SELECT preco FROM pizzas WHERE sabor = ? AND tamanho = ?", ("Mussarela", "Média"))
    row = cursor.fetchone()
    
    if row:
        print(f"Preço encontrado: {row['preco']}")
    else:
        print("Nenhum preço encontrado!")

# Chama a função para testar
test_query()
