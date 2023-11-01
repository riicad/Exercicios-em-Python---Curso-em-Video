Nome = str(input('Digite seu nome: ')).strip
Separar = Nome.split()
Primeiro = Separar[0]
print('Primeiro nome: {}'.format(Primeiro))
Espaço = Nome.rfind(' ')
Ultimo = Nome[Espaço:]
print('Ultimo nome:{}'.format(Ultimo))
