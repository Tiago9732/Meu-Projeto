class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def retirar_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            return False

    def calcular_subtotal(self, quantidade):
        return self.preco * quantidade


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


produtos = []
clientes = []
pedidos = []


def cadastrar_produto():
    print('\n===== CADASTRO DE PRODUTO =====')

    nome = input('Nome do produto: ')

    preco = float(input('Preço do produto: R$ '))

    estoque = int(input('Quantidade em estoque: '))

    produto = Produto(nome, preco, estoque)

    produtos.append(produto)

    print('\nProduto cadastrado com sucesso!')


def listar_produtos():
    print('\n===== PRODUTOS CADASTRADOS =====')

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return

    for i, produto in enumerate(produtos, start=1):
        print(f'\nProduto {i}')
        print(f'Nome: {produto.nome}')
        print(f'Preço: R$ {produto.preco:.2f}')
        print(f'Estoque: {produto.estoque}')


def cadastrar_cliente():
    print('\n===== CADASTRO DE CLIENTE =====')

    nome = input('Nome do cliente: ')
    telefone = input('Telefone: ')

    cliente = Cliente(nome, telefone)

    clientes.append(cliente)

    print('\nCliente cadastrado com sucesso!')


def listar_clientes():
    print('\n===== CLIENTES CADASTRADOS =====')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f'\nCliente {i}')
        print(f'Nome: {cliente.nome}')
        print(f'Telefone: {cliente.telefone}')


def fazer_pedido():
    print('\n===== NOVO PEDIDO =====')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        return

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return

    # Escolher cliente
    print('\nClientes:')

    for i, cliente in enumerate(clientes, start=1):
        print(f'{i} - {cliente.nome}')

    try:
        escolha_cliente = int(input('Escolha o cliente: '))
    except ValueError:
        print('Digite um número válido.')
        return

    if escolha_cliente < 1 or escolha_cliente > len(clientes):
        print('Cliente inválido.')
        return

    cliente = clientes[escolha_cliente - 1]

    # Lista de itens do pedido
    itens = []
    total_pedido = 0

    while True:
        print('\n===== PRODUTOS =====')

        for i, produto in enumerate(produtos, start=1):
            print(
                f'{i} - {produto.nome} '
                f'| R$ {produto.preco:.2f} '
                f'| Estoque: {produto.estoque}'
            )

        print('0 - Finalizar pedido')

        try:
            escolha_produto = int(input('Escolha o produto: '))
        except ValueError:
            print('Digite um número válido.')
            continue

        if escolha_produto == 0:
            break

        if escolha_produto < 1 or escolha_produto > len(produtos):
            print('Produto inválido.')
            continue

        produto = produtos[escolha_produto - 1]

        try:
            quantidade = int(input('Quantidade: '))
        except ValueError:
            print('Digite uma quantidade válida.')
            continue

        if quantidade <= 0:
            print('A quantidade deve ser maior que zero.')
            continue

        if not produto.retirar_estoque(quantidade):
            print('Quantidade indisponível em estoque.')
            continue

        subtotal = produto.calcular_subtotal(quantidade)

        item = {
            'produto': produto.nome,
            'quantidade': quantidade,
            'subtotal': subtotal
        }

        itens.append(item)

        total_pedido += subtotal

        print(f'Produto adicionado! Subtotal: R$ {subtotal:.2f}')

    if len(itens) == 0:
        print('Nenhum produto foi adicionado ao pedido.')
        return

    pedido = {
        'cliente': cliente.nome,
        'itens': itens,
        'total': total_pedido
    }

    pedidos.append(pedido)

    print('\n===== PEDIDO REALIZADO =====')
    print(f'Cliente: {cliente.nome}')

    for item in itens:
        print(
            f'{item["quantidade"]}x '
            f'{item["produto"]} '
            f'- R$ {item["subtotal"]:.2f}'
        )

    print(f'TOTAL: R$ {total_pedido:.2f}')


def listar_pedidos():
    print('\n===== PEDIDOS REALIZADOS =====')

    if len(pedidos) == 0:
        print('Nenhum pedido realizado.')
        return

    for i, pedido in enumerate(pedidos, start=1):
        print(f'\nPedido {i}')
        print(f'Cliente: {pedido["cliente"]}')

        for item in pedido['itens']:
            print(
                f'- {item["quantidade"]}x '
                f'{item["produto"]} '
                f'R$ {item["subtotal"]:.2f}'
            )

        print(f'TOTAL: R$ {pedido["total"]:.2f}')


def consultar_estoque():
    print('\n===== ESTOQUE =====')

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return

    for produto in produtos:
        print(
            f'{produto.nome} '
            f'- Estoque: {produto.estoque} unidades'
        )


def mostrar_menu():
    print('\n========================================')
    print('       COFFEE SHOPS TIA ROSA')
    print('========================================')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Cadastrar cliente')
    print('4 - Listar clientes')
    print('5 - Fazer pedido')
    print('6 - Listar pedidos')
    print('7 - Consultar estoque')
    print('0 - Sair')
    print('========================================')


while True:
    mostrar_menu()

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        cadastrar_produto()

    elif opcao == '2':
        listar_produtos()

    elif opcao == '3':
        cadastrar_cliente()

    elif opcao == '4':
        listar_clientes()

    elif opcao == '5':
        fazer_pedido()

    elif opcao == '6':
        listar_pedidos()

    elif opcao == '7':
        consultar_estoque()

    elif opcao == '0':
        print('Sistema encerrado.')
        break

    else:
        print('Opção inválida!')