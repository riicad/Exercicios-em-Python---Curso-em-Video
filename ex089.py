lista = [[[]]]


def linha():
    print('--' * 15)


while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    notas = [n1, n2]
    media = (n1 + n2) / 2

    lista.append(nome)
    lista[0].append(notas)
    lista[0][0].append(media)

    on = str(input('Quer continuar? [S/N] ')).upper()[0]
    if on == 'N':

        break

print('-=' * 20)
print(f'No. {"NOME": <10}  MÉDIA')
linha()

for i in range(0, len(lista) - 1):
    print(f'{i: <3} {lista[i + 1]: <11} {lista[0][0][i]}')

linha()


while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:

        print('Finalizando...')
        break

    print(f'Notas de {lista[n + 1]} são {lista[0][n + 1]}')
    linha()

print('>>> VOLTE SEMPRE <<<')
