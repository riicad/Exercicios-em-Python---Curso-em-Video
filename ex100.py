from random import randint
from time import sleep


def sorteio(lst):
    print(f'Os valores sorteados são ', end='')

    for i in range(0, 5):
        n = randint(0, 10)
        lst.append(n)

        sleep(0.6)
        print(n, end=' ', flush=True)

    print('.')


def somapar(lst):
    somar = int()

    for i in lst:
        if i % 2 == 0:

            somar += i

    print(f'Somando os valores pares de {num}, temos {somar}.')


num = list()
sorteio(num)
somapar(num)
