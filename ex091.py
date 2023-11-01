from random import randint
from time import sleep
from operator import itemgetter

valores = dict()

print('Valores sorteados: ')
for i in range(1, 5):
    valores[f"jogador {i}"] = randint(1, 6)

    print(f'  O jogador {i} tirou {valores[f"jogador {i}"]}')
    sleep(1)

ranking = dict()
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)

print('-=' * 20)
print('Ranking dos jogadores: ')

for k, v in enumerate(ranking):
    sleep(1)
    print(f'{k + 1}º lugar: {v[0]} com {v[1]} pontos.')

# lista = list(valores.values())
# lista.sort(reverse=True)
# keys = list()

#cont = 0

# for c in lista:
    # for k, v in valores.items():

        # if c == v and k not in keys:
            # keys.append(k)
            # cont += 1

            # sleep(1)
            # print(f'  {cont}° lugar: {k} com {v} pontos.')
