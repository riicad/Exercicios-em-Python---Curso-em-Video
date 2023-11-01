tuplas = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 20 >= n >= 0:
            break
        print('Tente Novamente.', end=' ')
    print(f'O número que você digitou é {tuplas[n]}')
    c = ' '
    while c not in 'SsNn':
        c = str(input('Deseja ver outro número? [S/N] '))[0]
    if c in 'Ss':
        print('Vamos de novo!', end=' ')
    else:
        break
print('Programa finalizado.')
