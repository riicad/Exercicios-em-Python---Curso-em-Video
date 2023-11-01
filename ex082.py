lista = list()
pares = list()
ímpar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    on = str(input('Quer continuar? [S/N] ')).upper()[0]
    if on == 'N':
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        ímpar.append(i)
print(f'{"LISTAS FINALIZADAS":-^40}')
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpar}')
