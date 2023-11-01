def leiaint(msg=''):
    """
    -> programa lê somente números inteiros.
    :param: msg: mensagem a ser mostrada na tela.
    return: retorna um valor inteiro.
    """
    cores = {'red': '\033[1;31m',
             'white': '\033[m'}

    while True:
        try:
            valor = int(input(msg))

        except KeyboardInterrupt:
            print(f'{cores["red"]}O usuário decidiu não digitar esse número.{cores["white"]}')
            return 0

        except (ValueError, TypeError):
            print(f'{cores["red"]}ERRO! Por favor, digite um número inteiro válido.{cores["white"]}')

        else:
            return valor


def leiafloat(msg=''):
    """
    -> programa lê somente números reais.
    :param: msg: mensagem a ser mostrada na tela.
    return: retorna um valor real.
    """
    cores = {'red': '\033[1;31m',
             'white': '\033[m'}

    while True:
        try:
            valor = float(input(msg))

        except KeyboardInterrupt:
            print(f'{cores["red"]}O usuário decidiu não digitar esse número.{cores["white"]}')
            return 0

        except (ValueError, TypeError):
            print(f'{cores["red"]}ERRO! Digite um valor inteiro válido.{cores["white"]}')

        else:
            return valor


i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')

print(f'O valor inteiro foi {i} e o número real foi {f}')
