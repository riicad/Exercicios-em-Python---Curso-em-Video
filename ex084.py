pessoa = list()
lista = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))

    lista.append(pessoa[:])
    pessoa.clear()

    on = str(input('Quer continuar? [S/N] ')).upper()[0]
    if on == 'N':
        break

print(f'Ao todo, você cadastrou {len(lista)} pessoas.')

valores = list()

for i in range(0, len(lista)):

    valores.append(lista[i][1])

maior = max(valores)
menor = min(valores)

print(f'O maior peso foi {maior}Kg. Peso de ', end='')

for n in lista:

    if n[1] == maior:

        print(f'[{n[0]}]', end=' ')

print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')

for n in lista:

    if n[1] == menor:

        print(f'[{n[0]}]', end='')
