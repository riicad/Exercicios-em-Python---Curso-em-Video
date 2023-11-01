def area(a, b):
    valor = a * b
    print(f'A area do terreno de {a}m x {b}m é de {valor:.2f}m^2')


print(f'{"CONTROLE DE TERRENOS": ^30}')
print('-' * 30)

lar = float(input('Largura (m): '))
com = float(input('Comprimento (c): '))

area(lar, com)
