from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 15)
    print(f'Contagem de {inicio} até {abs(fim)} de {abs(passo)} em {abs(passo)}:')

    if passo == 0:
        passo = 1

    if passo < 0:
        passo -= passo * 2

    c = inicio

    if inicio < fim:
        while c <= fim:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c += passo

    else:
        while c >= fim:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c -= passo

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')

contador(
    int(input('Início: ')),
    int(input('FIM:    ')),
    int(input('Passo:  '))
)
