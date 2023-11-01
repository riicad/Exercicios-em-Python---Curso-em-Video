número = int(input('Digite um número: '))
for x, i in enumerate(range(0, número * 10 + 1, número)):
    print(f'{número} x {x:2} = {i}')

