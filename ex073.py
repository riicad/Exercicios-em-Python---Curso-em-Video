tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio',
          'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR',
          'Ceará', 'Atlético-GO', 'Bragantino', 'Sport', 'Fortaleza', 'Vasco',
          'Bahia', 'Goiás', 'Botafogo', 'Coritiba')
print(f' Tabela do BRASILEIRÃO: ', end="")
for time in tabela:
    print(f'{time},', end=" ")
print('ACABOU.\n', '-=' * 20)
print(' Os cinco primeiros da tabela são: ', end="")
for time in tabela[0:5]:
    print(f'{time},', end=" ")
print('FIM.\n', '-=' * 20)
print(' Os 5 últimos da tabela são: ', end="")
for time in tabela[-4:]:
    print(f'{time},', end=" ")
print('FIM.\n', '-=' * 20)
print(' Tabela em ordem alfabética: ', end="")
for time in sorted(tabela):
    print(f'{time},', end=" ")
print('ACABOU.\n', '-=' * 20)
print(' Em que lugar esta a Chapecoense: não esta na tabela da série A. :c')
