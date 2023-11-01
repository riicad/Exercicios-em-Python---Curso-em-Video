z = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        z += c
print(f'A soma de todos os números ímpares que são múltiplos de 3 é {z}')
