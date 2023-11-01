def metade(n, f=False):
    m = n / 2

    if f:
        m = f'R${m:.2f}'

    return m


def dobro(n, f=False):
    d = n * 2

    if f:
        d = f'R${d:.2f}'

    return d


def aumentar(n, p=0, f=False):
    a = n + ((n * p) / 100)

    if f:
        a = f'R${a:.2f}'

    return a


def diminuir(n, p=0, f=False):
    d = n - ((n * p) / 100)

    if f:
        d = f'R${d:.2f}'

    return d


def moeda(n):
    return f'R${n:.2f}'


