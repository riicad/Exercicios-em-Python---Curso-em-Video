n = 0
for i in range(1, 7):
    número = int(input(f'Número {i}: '))
    if número % 2 == 0:
        n += número
print(f'A soma dos números pares é: {n}')
