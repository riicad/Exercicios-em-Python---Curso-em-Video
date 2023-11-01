pessoa = dict()
lista = list()
total = int()

while True:
    pessoa["nome"] = str(input('Nome: '))
    pessoa["sexo"] = str(input('Sexo [M/F]:  ')).upper()[0]

    while pessoa["sexo"] not in 'MF':
        print('ERRO! Responda apenas com M e F.')
        pessoa["sexo"] = str(input('Sexo [M/F]:  ')).upper()[0]  # while True funfa com um input

    pessoa["idade"] = int(input('Idade: '))

    total += pessoa["idade"]  # sum() soma os valores automaticamente
    lista.append(pessoa.copy())

    on = str(input('Quer continuar? [S/N] ')).upper()[0]

    while on not in 'SN':
        print('ERRO! Responda apenas com S e N.')
        on = str(input('Quer continuar? [S/N] ')).upper()[0]

    if on == 'N':
        break

print('-' * 60)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A média de idade é {total / len(lista):.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for i in lista:
    for k, v in i.items():

        if v == 'F':
            print(f'[{i["nome"]}]', end=' ')

print()
print('A lista de pessoas acima da média é: ')
print()
for i in lista:

    if i["idade"] >= (total / len(lista)):
        print(f'   => Nome: {i["nome"]} | Sexo: {i["sexo"]} | Idade: {i["idade"]}')

print("---->> ENCERRADO <<----")
