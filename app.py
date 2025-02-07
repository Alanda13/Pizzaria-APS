from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Função para conectar ao banco de dados
def get_db():
    conn = sqlite3.connect('pizzaria.db')
    conn.row_factory = sqlite3.Row  # Para retornar resultados como dicionários
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        bairro = request.form['bairro']

        # Conectar ao banco de dados e inserir as informações do cliente
        db = get_db()
        db.execute('INSERT INTO clientes (nome, telefone, endereco, bairro) VALUES (?, ?, ?, ?)',
                   (nome, telefone, endereco, bairro))
        db.commit()

        # Redirecionar para a tela de cadastro de pizza após cadastro do cliente
        return redirect('/cadastro_pizza')

    return render_template('cadastro_cliente.html')

@app.route('/cadastro_pizza', methods=['GET', 'POST'])
def cadastro_pizza():
    if request.method == 'POST':
        sabor = request.form['sabor']
        tamanho = request.form['tamanho']
        quantidade = int(request.form['quantidade'])

        # Buscar o preço da pizza no banco de dados baseado no sabor e tamanho
        db = get_db()
        cursor = db.execute('SELECT preco FROM pizzas WHERE sabor = ? AND tamanho = ?', (sabor, tamanho))
        resultado = cursor.fetchone()

        if resultado:
            preco = resultado['preco']
        else:
            preco = 0.0  # Se não encontrar, assume 0.0 como preço padrão

        print(f"Preço da pizza encontrado: R$ {preco}")  # DEBUG: Veja se está pegando o preço

        # Armazenando as variáveis na sessão
        session['sabor'] = sabor
        session['tamanho'] = tamanho
        session['quantidade'] = quantidade
        session['preco'] = preco

        return redirect(url_for('forma_pagamento'))
    
    return render_template('cadastro_pizza.html')


@app.route('/forma_pagamento', methods=['GET', 'POST'])
def forma_pagamento():
    if request.method == 'POST':
        sabor = session.get('sabor', '')
        tamanho = session.get('tamanho', '')
        quantidade = int(session.get('quantidade', 1))
        pagamento = request.form.get('pagamento', '')
        troco = request.form.get('troco', '')

        # Calcular o preço e total
        preco = float(session.get('preco', 0.0))
        total = preco * quantidade

        # Salvar no banco
        db = get_db()
        db.execute('INSERT INTO pedidos (sabor, tamanho, quantidade, preco, pagamento, troco) VALUES (?, ?, ?, ?, ?, ?)',
                   (sabor, tamanho, quantidade, preco, pagamento, troco))
        db.commit()

        return redirect(url_for('pedido_realizado'))

    # Se for GET, buscar os valores corretamente da sessão
    sabor = session.get('sabor', '')
    tamanho = session.get('tamanho', '')
    quantidade = int(session.get('quantidade', 1))

    # Buscar o preço correto do banco
    db = get_db()
    cursor = db.execute('SELECT preco FROM pizzas WHERE sabor = ? AND tamanho = ?', (sabor, tamanho))
    row = cursor.fetchone()

    if row:
        preco = float(row['preco'])
    else:
        preco = 0.0  # Se não encontrar, define como 0

    print(f"DEBUG - Sabor: {sabor}, Tamanho: {tamanho}, Quantidade: {quantidade}, Preço: {preco}")  # Depuração

    return render_template('forma_pagamento.html', sabor=sabor, tamanho=tamanho, quantidade=quantidade, preco=preco)

@app.route('/pedido_realizado')
def pedido_realizado():
    # Obtendo as informações da sessão
    sabor = session.get('sabor', '')
    tamanho = session.get('tamanho', '')
    quantidade = int(session.get('quantidade', 1))
    preco = float(session.get('preco', 0.0))

    # Calculando o total
    total = preco * quantidade
    pagamento = session.get('pagamento', '')
    troco = session.get('troco', '')

    return render_template('pedido_realizado.html', sabor=sabor, tamanho=tamanho, quantidade=quantidade, preco=preco, total=total, pagamento=pagamento, troco=troco)

if __name__ == '__main__':
    app.run(debug=True)

