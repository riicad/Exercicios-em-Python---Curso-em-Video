print('-='*9)
print('  Números primos')
print('-='*9)
número = int(input('Digite um número: '))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(3, 14, 2):
    if número % i in lista and número % 2 == 1 and i != 9:
        primo = f'O número {número} é primo.'
    elif número == 2 or número == 5:
        primo = f'O número {número} é primo.'
    elif número % 2 == 0 or número % 5 == 0:
        primo = f'O número {número} não é primo.'
print(primo)

#solução do Guanabara

'''
total = 0
número = int(input('Digite um número: '))
for i in range(1, número + 1):
    if i % == 0:
      print('\033[31m')
      total += 1
    else:
        print('\033[32m'
if total == 2:
    print(É primo)
else:
    print(Não é primo)'''