from datetime import date
ms = 0
mn = 0
for i in range(1, 8):
    ano = int(input(f'O ano de nascimento da {i}° pessoa: '))
    idade = abs(ano - date.today().year)
    if idade >= 21:
        ms += 1
    elif idade < 21:
        mn += 1
print(f'A quantidade de pessoas maiores de idade é: {ms}')
print(f'A quantidade de pessoas menores de idade é: {mn}')
