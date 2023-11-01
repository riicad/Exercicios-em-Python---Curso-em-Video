def ficha(nome='<desconhecido>', gols='0'):
    print('--'*20)
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)

else:
    g = 0

if n.strip() == '':
    ficha(gols=g)

else:
    ficha(n, g)

