Salário = float(input('Quanto é o seu salário? '))
Dez = Salário * 10 / 100
Quinze = Salário * 15 / 100
if Salário >= 1250.00:
    print('O valor do seu aumento é 10%, logo seu salário vai ser: R${:.2f}'.format(Salário + Dez))
else:
    print('O valor do seu aumento é 15%, logo seu salário vai ser: R${:.2f}'.format(Salário + Quinze))
