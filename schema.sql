-- Tabela para clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    bairro TEXT NOT NULL
);

-- Tabela para pizzas
CREATE TABLE IF NOT EXISTS pizzas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sabor TEXT NOT NULL,
    tamanho TEXT NOT NULL
);

-- Tabela para pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    pizza_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(id)
);
