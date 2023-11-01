jogador = dict()

jogador["nome"] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

jogador["gols"] = list()
jogador["total"] = int()

for p in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {p + 1}? '))

    jogador["gols"].append(gol)
    jogador["total"] += gol  # sum() soma os valores automaticamente

print('-' * 60)
print(jogador)
print('-' * 60)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('-' * 60)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i in range(0, partidas):
    print(f'{"=> ":>7}Na partida {i + 1} ele fez {jogador["gols"][i]}')
print(f'Um total de {jogador["total"]} gols')
