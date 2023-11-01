from time import sleep
Casa = float(input('Valor da casa: R$'))
Salário = float(input('Valor do seu salário: R$'))
Anos = int(input('Em quantos anos você vai querer pagar? '))
Mês = Anos * 12
Pres = Casa / Mês
Trinta = Salário * 30 / 100
print('Estamos verificando seu empréstimo.\nAguarde...')
sleep(2)
if Pres <= Trinta:
    print('{}ACEITO{}. O valor da parcela por mês sera de {}R${:.2f}'.format('\033[32m', '\033[0m', '\033[33m', Pres))
else:
    print('Seu empréstimo foi {}NEGADO{}.'.format('\033[31m', '\033[0m'))
