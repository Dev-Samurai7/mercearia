print('Bem vindo ao Controle De Estoque do José Lourenço da Conceição. RU 4154513')  # Identificação pessoal

print('============================================')
print('================ MERCEARIA =================')
print('============================================')


# Função para cadastrar Produto
def cadastrarProduto(codigo):
    print('Cadastrar Produto')
    listProdutos = {}
    produtos = []

    while True:
        try:
            codigo = int(input('Digite o Codigo do produto: '))
            break

        except:
            print('Digite somente numeros')
            continue

        nome = input('Digite o Nome do produto: ')
        fabricante = input('Digite o Fabricante do produto: ')

        try:
            valor = int(input('Digite o Valor do produto: '))

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
   


# Função para Consultar Produto
def consultaProduto(codigo):
    print('Adicionar Produto')


# Função para Remover Produto
def removerProduto(codigo):
    print('Remover Produto')


# Função para iniciar o programa

def menu():
    cont = 0
    print('Escolha a opção desejada \n'
          '1- Cadastrar Produto \n'
          '2- Consultar Produto \n'
          '3- Remover Produto \n'
          '0- Sair')

    while True:
        try:
            option = int(input('Digite a opção desejada: '))

            if option == 1:
                cont += 1
                cadastrarProduto(cont)

            elif option == 2:
                cont += 1
                consultaProduto(cont)

            elif option == 3:
                cont += 1
                removerProduto(cont)

            elif option == 0:
                print('SAINDO DO PROGRAMA...')
                break

            else:
                print('Opção invalida. Digite somete numeros de 1 - 3 \n')
                continue
        except ValueError:
            print('ERROR!!! Caracter invalido. Digite somente numeros de 1 - 3 \n')


def play():
    menu()


play()
