print("\033[35mDiga 3 segmentos de retas e eu vou calcular para ver se é possivel formar um triângulo.\033[m")
R1 = float(input('Primeira reta: '))
R2 = float(input('Segunda reta: '))
R3 = float(input('Terceira reta: '))
Yellow = '\033[1;33m'
White = '\033[m'
Green = '\033[32m'
Red = '\033[32m'
if abs(R2 - R3) < R1 < R2 + R3 or abs(R1 - R3) < R2 < R1 + R3 or abs(R2 - R1) < R3 < R2 + R1:
    print('{}É POSSÍVEL formar um triângulo.{}'.format(Green, White))
    if R1 == R2 == R3:
        print('Seu triângulo é {}EQUILÁTERO{}.'.format(Yellow, White))
    elif R1 == R2 != R3 or R1 == R3 != R2 or R2 == R1 != R3 or R2 == R3 != R1 or R3 == R2 != R1 or R3 == R1 != R2:
        print('Seu triângulo é {}ISÓSCELES{}.'.format(Yellow, White))
    else:
        print('Seu triângulo é {}ESCALENO{}.'.format(Yellow, White))
else:
    print('{}Não é possível formar um triângulo.'.format(Red))
