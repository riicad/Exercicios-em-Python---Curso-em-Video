Distância = float(input('Qual a distância da sua viagem? '))
Menor = Distância * 0.50
Maior = Distância * 0.45
if Distância <=200:
    print('O valor da sua distância é: R${:.2f}'.format(Menor))
else:
    print('O valor da sua distância é: R${:.2f}'.format(Maior))
