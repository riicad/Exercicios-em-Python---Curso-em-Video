lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não vou adicionar...')
    ligar = str(input('Você deseja continuar? [S/N] ')).upper()[0]
    if ligar == 'N':
        break
lista.sort()
print(f'{"PROGRAMA FINALIZADO":-^40}')
print(f'Você digitou os valores {lista}')
