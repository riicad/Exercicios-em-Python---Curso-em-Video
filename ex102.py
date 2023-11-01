def fat(n, show=False):
    """
    -> Programa calcula o fatorial de n.
    :param n: número a ser calculado (obrigatório).
    :param show: (opcional) Mostra ou não a conta.
    :return: Valor do fatorial de um número n.
    - Feito por Chuva⛱.
    """
    from math import factorial

    s = factorial(n)

    print('--' * 20)

    if show:
        for c in range(n, 1, -1):

            print(f' {c} x', end='')
        print(f' 1 = ', end='')

        return s

    else:
        return s


# programa principal
print(fat(7, show=True))
