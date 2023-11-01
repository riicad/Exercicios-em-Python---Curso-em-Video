lista = list()
jogador = dict()

while True:
    jogador["nome"] = str(input('Nome do jogador: '))

    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    jogador["gols"] = list()
    jogador["total"] = int()

    for p in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {p + 1}? '))

        jogador["gols"].append(gol)
        jogador["total"] += gol

    lista.append(jogador.copy())

    while True:
        on = str(input('Quer continuar? [S/N] ')).upper()[0]
        if on in 'SN':
            break

        print('ERRO!! Responda com S e N.')

    if on == 'N':
        break


def separador():
    print('-=' * 20)


separador()
print(f'{"Cod Nome":<15}{"Gols":<14}Total')
separador()

n = 0
for p in lista:
    print(f'{n} {p["nome"]:<11}{str(p["gols"]):<19}{p["total"]}')
    n += 1

while True:
    separador()
    dados = int(input('Mostrar dados de qual jogador? (999 para finalizar)'))

    if dados == 999:
        break

    elif dados > (n - 1):
        print(f'ERRO!! Não existe jogador {dados}. Tente novamente.')

    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[dados]["nome"]} ---')

        for i in range(0, len(lista[dados]["gols"])):
            print(f'   Na partida {i + 1} ele fez {lista[dados]["gols"][i]} gols.')
