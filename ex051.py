primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
print(f'Os 10 primeiros termos da sua PA: {primeiro}', "->", end=' ')
for i in range(1, 10):
    print(primeiro + (razão * i), '->', end=' ')
print("ACABOU")