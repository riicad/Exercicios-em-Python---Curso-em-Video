ligar = 'S'
somar = contar = 0
cores = {'Yellow': '\033[1;33m',
         'White': '\033[m'}
while ligar == 'S':
    número = int(input('Digite um número: '))
    contar += 1
    somar += número
    if contar == 1:
        maior = número
        menor = número
    if número > maior:
        maior = número
    if número < menor:
        menor = número
    ligar = str(input(f'{cores["Yellow"]}Quer continuar [S/N]? {cores["White"]}')).upper()
print(f'O maior número é: {cores["Yellow"]}{maior}{cores["White"]}')
print(f'O menor número é: {cores["Yellow"]}{menor}{cores["White"]}')
print(f'A média entre todos eles é: {cores["Yellow"]}{somar / contar}')
