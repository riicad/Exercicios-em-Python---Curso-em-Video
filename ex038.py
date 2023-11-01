primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro: '))
if primeiro > segundo:
    print('Maior número: {}{}\033[0m'.format('\033[33m', primeiro))
    print('Menor número: {}{}'.format('\033[33m', segundo))
elif segundo > primeiro:
    print('Maior número: {}{}\033[0m'.format('\033[33m', segundo))
    print('Menor número: {}{}'.format('\033[33m', primeiro))
else:
    print('{}Os dois valores são iguais.'.format('\033[33m'))
