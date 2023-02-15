from lib.arquivo import adicionar, exibir
from lib.autenticador import leiaNome, leiaInt
from lib.interface import menu, opçao


while True:
    menu()
    valor = opçao()
    if valor == 1:
        exibir()
    if valor == 2:
        nome = leiaNome('Nome: ')
        idade = leiaInt('Idade: ')
        adicionar(nome, idade)
    if valor == 3:
        break
