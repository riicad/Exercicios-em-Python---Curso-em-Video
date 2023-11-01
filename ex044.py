Preço = float(input('Preço das compras: R$'))
print('-='*18, '\n  {}Tabela de condições de pagamento{}'.format('\033[34m', '\033[m'))
print('''1 - À vista dinheiro/cheque.
2 - À vista no cartão.
3 - Em até 2x do preço normal.
4 - 3x ou mais no cartão.''')
print('-='*18)
Condição = float(input('{}Qual a condição de pagamento de acordo com o número na tabela? '.format('\033[33m')))
if Condição == 1:
    Valor = Preço * 10 / 100
    Desconto = Preço - Valor
elif Condição == 2:
    Valor = Preço * 5 / 100
    Desconto = Preço - Valor
elif Condição == 3:
    Desconto = Preço
    print('Você ira pagar em  duas vezes de R${:.2f}'.format(Preço/2))
elif Condição == 4:
    Valor = Preço * 20 / 100
    Desconto = Preço + Valor
    Vezes = int(input('Você quer parcelar em quantas vezes? '))
    print('Você ira pagar em {}x de R${:.2f}'.format(Vezes, Desconto / Vezes))
else:
    Desconto = Preço
    print('Opção de pagamento inválida. Tente novamente.')
print('O valor total a ser pago é: R${:.2f}'.format(Desconto))

