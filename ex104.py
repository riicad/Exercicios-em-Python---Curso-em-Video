def leiaint(msg):
    cores = {'red': '\033[1;31m',
             'white': '\033[m'}
    while True:

        s = input(msg)

        if not s.isnumeric():
            print(f'{cores["red"]}ERRO!! Digite um valor númerico válido.{cores["white"]}')

        else:
            break

    return s


# programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
