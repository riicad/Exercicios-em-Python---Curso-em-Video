while True:
    número = int(input('Você quer ver tabuada de qual número? '))
    if número < 0:
        break
    print(' - =' * 5)
    for i in range(1, 11):
        print(f'   {número} x {i:2} = {número * i}   ')
    print(' - =' * 5)
