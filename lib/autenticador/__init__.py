def leiaInt(msg, intervalo = False):
    valido = False
    while not valido:
        try:
            escolha = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro...')
            continue
        else:
            if intervalo == False:
                return escolha
            else:
                if escolha in range(1, 4):
                    valido = True
                    return escolha
                else:
                    print('ERRO! Digite um número inteiro entre 1 e 3...')


def leiaNome(msg):
    while True:
        try:
            entrada = str(input(msg)).strip()
        except:
            print('ERRO! Digite um nome válido... ')
            continue
        else:
            nome_sobrenome = entrada.split()
            pontos_validos = 0
            cont = 0
            for cont in range(0, len(nome_sobrenome)):
                if nome_sobrenome[cont].isalpha():
                    pontos_validos += 1
                    if nome_sobrenome[cont] not in ('de', 'da', 'das', 'do', 'dos', 'e'):
                        nome_sobrenome[cont] = nome_sobrenome[cont].capitalize()

            if pontos_validos == len(nome_sobrenome):
                nome_full = ' '.join(nome_sobrenome)
                break
            else:
                print('ERRO! Digite um nome válido... ')
    return nome_full

     