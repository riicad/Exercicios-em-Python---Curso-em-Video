from time import sleep
from random import randint
pessoa = 0
tentativas = 0
computador = 0
cores = {'White': '\033[m',
         'Yellow': '\033[0;33m',
         'Pink': '\033[1;35m',
         'Green': '\033[1;32m',
         'Red': '\033[1;31m'}
print(f'{cores["Yellow"]}-=' * 12, f'\n {cores["Pink"]}  jogo de Adivinhação', '\n', f'{cores["Yellow"]}-=' * 12)
sleep(2)
print(f'{cores["White"]}PC: Vou pensar em um número entre 0 e 10...')
for i in range(2):
    print(f'{cores["Yellow"]}Aguarde...')
    sleep(1)
computador = randint(0, 10)
print(f'{cores["Green"]}Pronto!{cores["White"]}')
while pessoa != computador:
    pessoa = int(input('Em que número o computador pensou? '))
    tentativas += 1
    if pessoa != computador:
        print(f'Resposta{cores["Red"]} INCORRETA{cores["White"]}, tente novamente.')
print(f'PARABÉNS! resposta {cores["Green"]}CORRETA{cores["White"]}! O computador pensou no número {computador}.')
print(f'Total de tentativas: {cores["Yellow"]}{tentativas} ')
