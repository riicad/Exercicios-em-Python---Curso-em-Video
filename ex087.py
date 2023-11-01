valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

s = t = int()


def separador():
    print('-=' * 20)


for i in range(0, 3):  # linhas
    for c in range(0, 3):  # colunas

        valores[i][c] = int(input(f'Digite um valor para a posição [{i}, {c}]: '))

        if valores[i][c] % 2 == 0:  # calcula se é par
            s += valores[i][c]

        if c >= 2:  # calcula os valores da terceira coluna
            t += valores[i][2]

separador()

for v in valores:
    print(f'{f"{v}": ^40}')

separador()

print(f'A soma dos valores pares é {s}.')
print(f'A soma dos valores da terceira coluna é {t}.')
print(f'O maior valor da segunda linha é {max(valores[1])}')
