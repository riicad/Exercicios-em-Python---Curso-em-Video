primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print(f'{primeiro} -> ', end="")
contador = 0
while contador != 9:
    contador += 1
    print(primeiro + razão * contador, end=' -> ')
print('FIM')
