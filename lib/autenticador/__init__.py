def leiaInt(msg):
    valido = False
    while not valido:
        try:
            escolha = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro entre 1 e 3...')
            continue
        else:
            if escolha in range(1, 4):
                valido = True
                return escolha
            else:
                print('ERRO! Digite um número inteiro entre 1 e 3...')


      