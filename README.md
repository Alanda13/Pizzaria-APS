# Sistema de Controle de Pizzaria de Entrega em Domicílio

Este projeto visa a modelagem e desenvolvimento de um sistema de controle para uma pizzaria de entrega em domicílio. O sistema permite que o atendente registre os pedidos de pizzas, incluindo informações sobre o cliente, a escolha do sabor e o tamanho das pizzas, além de gerenciar o banco de dados e a interface gráfica do sistema.

## Funcionalidades

- **Cadastro de Cliente**: O atendente pode registrar os dados do cliente, como nome, endereço e telefone.
- **Anotação de Pedido**: O atendente registra o pedido do cliente, incluindo o sabor e o tamanho das pizzas.
- **Opções de Tamanho**: Cada pizza pode ser de um dos seguintes tamanhos: média, grande ou gigante.
- **Tela de Login**: Uma tela de login será implementada para garantir o acesso seguro ao sistema.
- **Interface Gráfica**: A interface gráfica do sistema será desenvolvida utilizando HTML, CSS e Django.
- **Banco de Dados**: O banco de dados será criado utilizando MongoDB ou PostgreSQL, conforme necessário.

## Requisitos

- Python 3.x
- Django
- MongoDB ou PostgreSQL
- HTML, CSS

## Estrutura do Projeto

- **/pizzaria**: Diretório principal do projeto Django.
  - **/models.py**: Modelos de dados, incluindo informações sobre o cliente e o pedido.
  - **/views.py**: Lógica de visualização para as páginas do sistema.
  - **/urls.py**: Configuração das URLs do sistema.
  - **/templates/**: Arquivos HTML para a interface gráfica.
  - **/static/**: Arquivos CSS para o estilo da aplicação.

## Casos de Uso


## Diagramas de Sequência

## Implementação das Classes

A seguir, serão implementadas as classes responsáveis pela gestão dos dados de clientes e pedidos.

- **Classe Cliente**: Responsável por armazenar as informações do cliente.
- **Classe Pedido**: Responsável por armazenar os detalhes do pedido, incluindo pizzas e cliente.

## Método de Escolha

Será implementado um método para calcular o preço total do pedido com base no tamanho das pizzas e o número de unidades.

## Interface Gráfica

A interface será desenvolvida em HTML e CSS para garantir uma experiência de usuário intuitiva. Ela incluirá formulários para cadastro de clientes e anotações de pedidos.

## Banco de Dados

O banco de dados será projetado para armazenar as informações sobre clientes e pedidos. Será utilizado o MongoDB ou PostgreSQL, dependendo das necessidades do projeto.


