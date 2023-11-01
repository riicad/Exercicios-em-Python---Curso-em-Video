número = int(input('Digite um número qualquer: '))
print('\033[1;31m-='*10)
print('\033[1;35mTabela de Conversão\033[m')
print('1 = Binário\n2 = Octa\n3 = Hexadecimal')
print('\033[1;31m-='*10, '\033[m')
base = int(input('Digite sua opção: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(número, bin(número)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, oct(número)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(número, hex(número)[2:]))
else:
    print('Opção inválida. Tente novamente.')
