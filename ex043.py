print('\033[34m=-'*8)
print('\033[1;35mVerificador IMC\033[m')
print('\033[34m=-'*8, '\033[m')
Altura = float(input('Digite sua altura: '))
Peso = float(input('Digite seu peso: '))
IMC = Peso/Altura**2
if IMC <= 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < IMC < 25:
    print('Você está no peso ideial.')
elif 30 >= IMC >= 25:
    print('Você está sobrepeso')
elif 30 < IMC <=40:
    print('Você tem obesidade.')
else:
    print('Você tem obesidade mórbida.')
