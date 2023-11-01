from datetime import date
print('\033[34m='*21)
print('\033[1;36mCATEGORIA DE NATAÇÃO.')
print('\033[34m='*21, '\033[m')
Ano = int(input('Ano de nascimento: '))
Idd = abs(Ano - date.today().year)
if Idd <= 9:
    categoria = 'MIRIM'
elif 9 < Idd <= 14:
    categoria = 'INFANTIL'
elif 14 < Idd <= 19:
    categoria = 'JUNIOR'
elif Idd == 20:
    categoria = 'SENIOR'
else:
    categoria = 'Master'
print('Você tem \033[33m{}\033[m anos, logo sua categoria é: \033[1;35m{}'.format(Idd, categoria))
