print('\033[33m-='*10)
print('\033[1;35m       Média')
print('\033[33m-='*10, '\033[m')
primeiro = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
média = (primeiro + segunda)/2
print('Sua média é: {}{:.1f}{}'.format('\033[35m', média, '\033[m'))
if média < 5:
    print('Você foi {}REPROVADO{}!'.format('\033[1;31m', '\033[m'))
elif 5 <= média <= 6.9:
    print('Você está de {}RECUPERAÇÃO{}!'.format('\033[1;33m', '\033[m'))
else:
    print('Você foi {}APROVADO{}!'.format('\033[1;32m', '\033[m'))
