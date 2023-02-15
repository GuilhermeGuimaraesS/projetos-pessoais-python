from lib.autenticador import leiaInt


def title(msg):
    """
    -> Recebe uma mensagem e mostra ela na tela centralizada entre 40 espaços com linhas em cima e embaixo
    :param msg: mensagem que será mostrada na tela
    Função criada por Guilherme Guimarães dos Santos
    """
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


def menu(funçoes = ['Vizualizar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']):
    """
    -> Função que recebe uma lista com as funções do sistema e exibe um menu de escolha na tela
    :param funçoes: Recebe uma lista com as funcionalidades do sistema
    Função criada por Guilherme Guimarães dos Santos
    """
    title('MENU PRINCIPAL')
    c = 1
    for item in funçoes:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print('-' * 50)
        

def opçao():
    """
    -> Função que recebe uma lista com as funções do sistema e exibe um menu de escolha na tela
    :param funçoes: Recebe uma lista com as funcionalidades do sistema
    Função criada por Guilherme Guimarães dos Santos
    """
    num = leiaInt('Sua opção: ', intervalo=True)
    if num == 1:
        title('PESSOAS CADASTRADAS')
    elif num == 2:
        title('NOVO CADASTRO')
    else:
        title('SAINDO DO SISTEMA... ATÉ MAIS!')
    return num
