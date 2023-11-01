from datetime import date
Ano = int(input('Digite um ano ou digite 0 para ver se o ano atual é bissexto: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('Seu ano é bissexto!')
else:
    print('Seu ano não é bissexto.')
