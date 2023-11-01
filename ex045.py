from random import choice
from time import sleep
print('\033[31m -'*5, '\n\033[33m  Jokenpô', '\n\033[36m','- '*5, '\033[m')
print('  \033[33mTabela\033[m\n - Papel\n - Pedra\n - Tesoura\n\033[36m','- '*5)
Número = str(input('\033[33mDigite o que você escolheu: \033[m')).title()
Computador = choice(['Pedra', 'Papel', 'Tesoura'])
sleep(1)
print('\033[31mJO')
sleep(1)
print('\033[33mKEN')
sleep(1)
print('\033[32mPÔ!!\033[m')
if Número == Computador:
    print('\033[1;33mEMPATE\033[m! Os dois escolheram: \033[33m{}'.format(Número))
elif Número == 'Tesoura' and Computador == 'Papel' or Número == 'Pedra' and Computador == 'Tesoura':
    print('PARABÉNS, você \033[1;32mGANHOU\033[m! O computador escolheu: \033[33m{}'.format(Computador))
elif Número == 'Papel' and Computador == 'Pedra':
    print('PARABÉNS, você \033[1;32mGANHOU\033[m! O computador escolheu: \033[33m{}'.format(Computador))
else:
    print('QUE PENA, você \033[1;31mPERDEU\033[m! O computador escolheu \033[33m{}'.format(Computador))


