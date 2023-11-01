from random import randint
tuplas = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print(f'Números gerados: ', end='')
for n in tuplas:
    print(f'{n}', end=' ')
print(f'\nMaior número: {max(tuplas)}')
print(f'Menor número: {min(tuplas)}')

print(sorted(tuplas))

