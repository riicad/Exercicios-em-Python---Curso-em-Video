from math import factorial
número = int(input('Digite um número: '))
print('O fatorial do seu número é: ')
contador = número
fatorial = factorial(número)
print(número, end='')
while contador != 1:
    contador -= 1
    print(' x', f'{contador}', end='')
print(f' = {fatorial}')
