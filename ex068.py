from random import randint
cores = {'y': '\033[1;33m',
         'g': '\033[1;32m',
         'r': '\033[1;31m',
         'w': '\033[m'}
vítorias = 0
print(f'{cores["y"]}--' * 15, '\n     Jogo de PAR ou IMPAR')
while True:
    print(f'{cores["y"]}--' * 15, f'{cores["w"]}')
    pessoa = int(input('Digite um número de 0 a 10: '))
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = randint(0, 10)
    resultado = pessoa + computador
    if resultado % 2 == 0:
        resposta = 'PAR'
    else:
        resposta = 'IMPAR'
    print(f'{cores["y"]}--' * 33, f'{cores["w"]}')
    print(f'Você jogou {pessoa} e o computador jogou {computador}. O total deu {resultado}, é {resposta}.')
    print(f'{cores["y"]}--' * 33, f'{cores["w"]}')
    if escolha[0] == resposta[0]:
        vítorias += 1
        print(f'Você {cores["g"]}VENCEU{cores["w"]}!\nVamos jogar novamente...')
    else:
        break
print(f'Você {cores["r"]}PERDEU{cores["w"]}!\nFIM de jogo. Você venceu {cores["y"]}{vítorias}{cores["w"]} vezes.')
