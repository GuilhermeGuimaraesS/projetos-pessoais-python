from time import sleep

def adicionar(nome, idade):
    """
    -> Função que recebe o nome e a idade que foram lidas e guardadas em duas variáveis e cadastra a pessoa no arquivo de notas. A função tenta criar o arquivo e cadastrar as informações, caso o arquivo já exista ele apenas adiciona as informações fornecidas
    """
    try:
        with open('Cadastro.txt', 'x') as arquivo:
            arquivo.write(f'{nome.ljust(40)} {idade} anos')
    except:
        with open('Cadastro.txt', 'a') as arquivo:
            arquivo.write(f'\n{nome.ljust(40)} {idade} anos')
    sleep(1)
    
    
def exibir():
    """
    -> Função que exibe as pessoas cadastradas no sistema
    """
    with open('Cadastro.txt', 'r') as arquivo:
        ficha = arquivo.read()
    print(ficha)
    sleep(1)
    
    