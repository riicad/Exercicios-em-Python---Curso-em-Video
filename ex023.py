número = int(input('Digite um número de 0 a 9999: '))
Dividir = str(número/1000)
Zero = (Dividir + '0')
Unidade = Zero[4]
Dezena = Zero[3]
Centena = Zero[2]
Milhar = Zero[0]
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(Unidade, Dezena, Centena, Milhar))

