def metade(n, f=False):
    m = n / 2

    if f:
        m = f'R${m:.2f}'.replace('.', ',')

    return m


def dobro(n, f=False):
    d = n * 2

    if f:
        d = f'R${d:.2f}'.replace('.', ',')

    return d


def aumentar(n, p, f=False):
    a = n + ((n * p) / 100)

    if f:
        a = f'R${a:.2f}'.replace('.', ',')

    return a


def diminuir(n, p, f=False):
    d = n - ((n * p) / 100)

    if f:
        d = f'R${d:.2f}'.replace('.', ',')

    return d


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, a, r):

    print('', '-'*30, f'\n{"RESUMO DO VALOR": ^30}\n', '-'*30)
    print(f' {"Preço analisado:":<20}{moeda(n)}')
    print(f' {"Dobro do preço:":<20}{dobro(n, True)}')
    print(f' {"Metade do preço:":<20}{metade(n, True)}')
    print(f' {f"Aumento de {a}%:":<20}{aumentar(n, a, True)}')
    print(f' {f"Redução de {r}%:":<20}{diminuir(n, r, True)}')
    print('', '-'*30)
