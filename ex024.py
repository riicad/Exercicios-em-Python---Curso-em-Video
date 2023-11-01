Cidade = str(input('Qual o nome da sua cidade? ')).strip()
Acima = Cidade.upper()
Separar = Acima.split()
Ler = Separar[0]
Tem = 'SANTO' in Ler[0:]
print('Existe a palavra "SANTO" no começo? \n{}'.format(Tem))
