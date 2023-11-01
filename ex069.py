maior = homem = mulher = 0
while True:
    print(f'{"CADASTRE UMA PESSOA":-^30}')
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade > 20:
        mulher += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{"PROGRAMA FINALIZADO":-^30}')
print(f'Total de pessoas maiores de idade: {maior}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres cadastradas: {mulher}')
