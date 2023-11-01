from random import randint
from time import sleep

valores = []


def linha():
    print('--' * 20)


linha()
print(f'{"MEGA SENA": ^40}')
linha()

n = int(input('Quantos jogos você vai querer que eu sorteie? '))

print(f'{f" SORTEANDO {n} JOGOS ":-^40}')

for i in range(0, n):

    while len(valores) < 6:
        valor = randint(0, 61)

        if valor not in valores:
            valores.append(valor)

    valores.sort()

    print(f'Jogo {i + 1}: {valores}')
    sleep(1)

    valores.clear()

print(f'{" < BOA SORTE > ":-^40}')
