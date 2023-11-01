menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')











'''p = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    p[i] = peso + 0
for c in range(1, 6):
    if p[1] > p[c] > p[2]:
        maior = p[1]
        menor = p[2]
    elif p[2] > p[c] > p[1]:
        maior = p[2]
        menor = p[1]
    elif p[3] > p[c] > p[1]:
        maior = p[3]
        menor = p[1]
    elif p[4] > p[c] > p[1]:
        maior = p[4]
        menor = p[1]
    elif p[5] > p[c] > p[1]:
        maior = p[5]
        menor = p[1]
    elif p[3] > p[c] > p[2]:
        maior = p[3]
        menor = p[2]
    elif p[4] > p[c] > p[2]:
        maior = p[4]
        menor = p[2]
    elif p[5] > p[c] > p[2]:
        maior = p[5]
        menor = p[2]
    elif p[1] > p[c] > p[3]:
        maior = p[1]
        menor = p[3]
    elif p[2] > p[c] > p[3]:
        maior = p[2]
        menor = p[3]
    elif p[4] > p[c] > p[3]:
        maior = p[4]
        menor = p[3]
    elif p[5] > p[c] > p[3]:
        maior = p[5]
        menor = p[3]
    elif p[1] > p[c] > p[4]:
        maior = p[1]
        menor = p[4]
    elif p[2] > p[c] > p[4]:
        maior = p[2]
        menor = p[4]
    elif p[3] > p[c] > p[4]:
        maior = p[3]
        menor = p[4]
    elif p[5] > p[c] > p[4]:
        maior = p[5]
        menor = p[4]
    elif p[1] > p[c] > p[5]:
        maior = p[1]
        menor = p[5]
    elif p[2] > p[c] > p[5]:
        maior = p[2]
        menor = p[5]
    elif p[3] > p[c] > p[5]:
        maior = p[3]
        menor = p[5]
    elif p[4] > p[c] > p[5]:
        maior = p[4]
        menor = p[5]
print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')'''

