Nome = str(input('Digite seu nome: ')).strip()
Caracteres = int(len(Nome))
Espaços = Nome.count(' ')
Total = (Caracteres - Espaços)
print('A quantidade de letras no nome é: {}'.format(Total))
Acima = Nome.upper()
print('O nome apenas com letras maiúsculas fica: {}'.format(Acima))
Abaixo = Nome.lower()
print('O nome com letras minúsculas fica: {}'.format(Abaixo))
Dividir = Nome.split()
Primeiro = len(Dividir[0])
print('A quantidade de letras do primeiro nome é: {}'.format(Primeiro))



