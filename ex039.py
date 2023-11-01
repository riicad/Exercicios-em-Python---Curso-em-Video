from datetime import date
print('\033[3;32m+ * '*5)
print('\033[36mAlistamento Militar')
print('\033[3;32m+ * '*5, '\033[m')
Ano = int(input('Digite o ano que você nasceu: '))
Idd = abs(Ano - date.today().year)
print('Você tem {} anos.'.format(Idd))
if Idd > 18:
    print('Você ja deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(abs(Idd - 18), Ano + 18))
elif Idd < 18:
    print('Você ainda não tem idade para se alistar. Faltam {} anos para seu alistamento.'.format(abs(Idd - 18)))
    print('Seu alistamento será em {}.'.format(Ano + 18))
else:
    print('Você esta exatamente na idade de se {}ALISTAR{}!!'.format('\033[1;32m', '\033[m'))