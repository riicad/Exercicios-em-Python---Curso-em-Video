tuplas = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {tuplas}')
print(f'O valor 9 apareceu {tuplas.count(9)} vezes.')
if 3 in tuplas:
    print(f'A valor 3 foi digitado em {tuplas.index(3) + 1}° lugar.')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in tuplas:
    if n % 2 == 0:
        print(n, end=' ')
