Velocidade = float(input('Digite a velocidade do seu carro:'))
Multa = (Velocidade - 80)*7
if Velocidade > 80.0:
    print('Você acabou de ser MULTADO.')
    print('O valor da sua multa é de R${:.2f}'.format(Multa))
else:
    print('Você esta na velocidade correta, continue assim.')
