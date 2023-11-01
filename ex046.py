from time import sleep
Cores = {'red': '\033[1;31m',
         'pink': '\033[1;35m',
         'white': '\033[m'}
print(f'{Cores["pink"]}-=' * 20, f'\n{Cores["red"]}Contagem para os fogos de artifício')
print(f'{Cores["pink"]}-=' * 20, f'{Cores["white"]}')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(f'{Cores["red"]}BOOOM!!')
