primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print(f'{primeiro} -> ', end="")
contador = 0
while contador != 9:
    contador += 1
    PA = primeiro + razão * contador
    print(PA, end=' -> ')
print('FIM')
print(f'Esses foram os 10 primeiros termos.', end=" ")
continuar = 'S'
while continuar != 'N':
    continuar = str(input('Deseja ver mais termos [S/N]? ')).upper()
    if continuar == 'S':
        quantidade = int(input('Quantos termos a mais você quer? '))
        for i in range(1, quantidade + 1):
            print(PA + razão * i, end=' -> ')
        print('FIM')
print('PROGRAMA FINALIZADO')
