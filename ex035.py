R1 = float(input('Primeira reta: '))
R2 = float(input('Segunda reta: '))
R3 = float(input('Terceira reta: '))
if abs(R2 - R3) < R1 < R2 + R3:
    print("É possível formar um triângulo!")
else:
    if abs(R1 - R3) < R2 < R1 + R3:
        print('É possível formar um triângulo!')
    else:
        if abs(R2 - R1) < R3 < R1 + R2:
            print('É possível formar um triângulo!')
        else:
            print('Não é possível formar um triângulo!')

