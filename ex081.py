lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    on = str(input('Quer continuar? [S/N] ')).upper()[0]
    if on == 'N':
        break
lista.sort(reverse=True)
print(f'{"LISTA FINALIZADA":=^30}')
print(f'Foram digitados {len(lista)} elementos.')
print(f'Lista de valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
