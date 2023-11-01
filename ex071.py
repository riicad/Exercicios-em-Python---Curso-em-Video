cores = {'y': '\033[1;33m',
         'w': '\033[m',
         'g': '\033[1;32m'}
print('', '=' * 29, f'\n{cores["y"]}{"BANCO DO BRASIL": ^30}', f'\n{cores["w"]}', f'=' * 29)
while True:
    valor = int(input(f' Valor a ser sacado: R$'))
    cinquenta = valor // 50
    vinte = (valor - 50 * cinquenta) // 20
    dez = ((valor - 50 * cinquenta) - 20 * vinte) // 10
    um = (((valor - 50 * cinquenta) - 20 * vinte) - 10 * dez) // 1
    if cinquenta != 0:
        print(f' Total de cédulas de R$50: {cores["y"]}{cinquenta}{cores["w"]}')
    if vinte != 0:
        print(f' Total de cédulas de R$20: {cores["y"]}{vinte}{cores["w"]}')
    if dez != 0:
        print(f' Total de cédulas de R$10: {cores["y"]}{dez}{cores["w"]}')
    if um != 0:
        print(f' Total de cédulas de R$1: {cores["y"]}{um}{cores["w"]}')
    print(f' Seu saque foi efetuado com {cores["g"]}sucesso.{cores["w"]}')
    print('', '=' * 29)
    novo = str(input(' Quer fazer outro saque? [S/N] ')).upper().strip()
    print('', '=' * 30)
    if novo in 'Nn':
        break
print(' Agradeçemos pela preferencia. Volte sempre.')
