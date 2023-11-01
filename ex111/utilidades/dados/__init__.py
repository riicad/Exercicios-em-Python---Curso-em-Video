def metade(n, f=False):
    """
    -> Função calcúla metade de um número.
    :param: n: número a ser calculado.
    :param: f: formata o valor n em BRL.(opcinal)
    :return: retorna metade do valor.
    """
    m = n / 2

    return m if f is False else moeda(m)


def dobro(n, f=False):
    """
    -> Função calcúla dobro de um número.
    :param: n: número a ser calculado.
    :param: f: formata o valor n em BRL.(opcinal)
    :return: retorna dobro do valor.
    """
    d = n * 2

    return d if f is False else moeda(d)


def aumentar(n, p, f=False):
    """
    -> Função aumenta o número de acordo com a porcentagem escolhida.
    :param: n: número a ser calculado.
    :param: p: porcentagem a ser aumentada.
    :param: f: formata o valor n em BRL.(opcinal)
    :return: retorna o valor mais porcentagem.
    """
    a = n + ((n * p) / 100)

    return a if not f else moeda(a)


def diminuir(n, p, f=False):
    """
    -> Função diminui o número de acordo com a porcentagem escolhida.
    :param: n: número a ser calculado.
    :param: p: porcentagem a ser reduzida.
    :param: f: formata o valor n em BRL.(opcinal)
    :return: retorna o valor menos porcentagem.
    """
    d = n - ((n * p) / 100)

    return d if not f else moeda(d)


def moeda(n, m='R$'):
    """
    -> Função formata o valor n em monetário.
    :param: n: valor a ser formatado.
    :param: m: moeda a ser escolhida. (Padrão: 'R$')
    :return: retorna valor formatado.
    """
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n, a, r):
    """
    -> Resumo de todas funções.
    :param: n: número a ser calculado.
    :param: a: porcentagem a ser aumentada.
    :param: r: porcentagem a ser reduzida.
    :return: retorna um resumo da analise do valor.
    """

    print('', '-'*30, f'\n{"RESUMO DO VALOR": ^30}\n', '-'*30)
    print(f' {"Preço analisado:":<20}{moeda(n)}')
    print(f' {"Dobro do preço:":<20}{dobro(n, True)}')
    print(f' {"Metade do preço:":<20}{metade(n, True)}')
    print(f' {f"Aumento de {a}%:":<20}{aumentar(n, a, True)}')
    print(f' {f"Redução de {r}%:":<20}{diminuir(n, r, True)}')
    print('', '-'*30)


def leiadinheiro(msg=''):
    """
    -> Função que lê apenas valor monetário.
    :param: msg: mensagem a ser passada no input.
    :return: retorna o valor monetário/númerico.
    """
    cores = {'red': '\033[1;31m',
             'white': '\033[m'}

    while True:
        ler = str(input(msg)).replace(',', '.').strip()

        if ler.isalpha() or ler == '':
            print(f'{cores["red"]}ERRO! \"{ler}\" não é um valor monetário válido.{cores["white"]}')

        else:
            return float(ler)

