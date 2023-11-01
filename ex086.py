valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for c in range(0, 3):

        valores[i][c] = int(input(f'Digite um número para a posição [{i}, {c}]: '))

for v in valores:
    print(f'{v}')
