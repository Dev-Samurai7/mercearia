print('Bem vindo ao Reustaurante do José Lourenço da Conceição. RU 4154513') #Identificação pessoal

print('============================================')
print('================ MERCEARIA =================')
print('============================================')

def mercearia():
    print('Escolha a opção desejada')
    print('1- Cadastrar Produto')
    print('2- Consultar Produto')
    print('Remover Produto')

def cadastrarProduto():
    global  listProdutos
    global produtos
    listProdutos = []
    produtos = {}

    while True:
        try:
            produtos['Codigo'] = (int(input('Digite o Codigo do produto: ')))

        except:
            print('Digite somente numeros')
            continue

        produtos['nome'] = (input('Digite o Nome do produto: '))
        produtos['Fabricante'] = (input('Digite o Fabricante do produto: '))

        try:
            produtos['valor'] = (int(input('Digite o Valor do produto: ')))

        except:
            print('Digite somente numeros')
            print('')
            continue


        try:
            more = int(input('Deseja cadastrar mais algum produto? 1 - SIM / 2 Não'))
            if more == 1:
                continue
            else:
                break
        except ValueError:
            print('Digite somente numeros')
            print('')
            continue

    listProdutos.append(produtos)
    return listProdutos

cadastrarProduto()

print(listProdutos)

# def consultarProduto(todos, codigo, fabricante):
#     def listaTodos ():
#         for i in listProdutos:
#             print(i)
#
#     todos = listaTodos()
#
#     def list