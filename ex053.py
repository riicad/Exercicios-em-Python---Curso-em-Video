cores = {'White': '\033[m',
         'Yellow': '\033[1;33m',
         'Green': '\033[1;32m',
         'red': '\033[1;31m'}
print(f'-='*20)
print(f'{cores["Yellow"]}Verificador de Políndromos')
print(f'{cores["White"]}-='*20)
frase = str(input('Digite uma frase: '))
rever = frase.replace(' ', '').upper()
contr = rever[::-1].upper()
if rever == contr:
    print(f'A frase: "{frase}" {cores["Green"]}É{cores["White"]} um POLÍNDROMO.')
else:
    print(f'A frase: "{frase}" {cores["red"]}NÃO{cores["White"]} é um POLÍNDROMO.')
