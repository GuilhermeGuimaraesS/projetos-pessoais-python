from lib.autenticador import leiaInt


def title(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


def menu(funçoes = ['Vizualizar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']):
    from lib.autenticador import leiaInt
    title('MENU PRINCIPAL')
    c = 1
    for item in funçoes:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print('-' * 40)
        

def opçao():
    num = leiaInt('Sua opção: ')
    if num == 1:
        title('PESSOAS CADASTRADAS')
    elif num == 2:
        title('NOVO CADASTRO')
    else:
        title('SAINDO DO SISTEMA... ATÉ MAIS!')
    return num
