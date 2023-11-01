valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {i}: ')))
print('-=' * 30)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor é {max(valores)}, ele está nas posições', end=' ')
for pos, val in enumerate(valores):
    if val == max(valores):
        print(pos, end='... ')
print()
print(f'O menor valor é {min(valores)}, ele está nas posições', end=' ')
for pos, val in enumerate(valores):
    if val == min(valores):
        print(pos, end='... ')
print()
