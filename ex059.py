from time import sleep
cores = {'White': '\033[m',
         'Yellow': '\033[1;33m',
         'Pink': '\033[1;35m',
         'Red': '\033[1;31m'}
opcão = 0
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
sleep(1)
print(f'''{cores["Yellow"]}  -- Menu de opcões --
   {cores["Pink"]}[1] Somar
   [2] Multiplicar
   [3] Maior
   [4] Novos números
   [5] Sair do programa''')
opcão = int(input(f'{cores["Yellow"]}Escolha uma opcão: {cores["White"]}'))
while opcão in [1, 2, 3, 4]:
    if opcão == 1:
        somar = num1 + num2
        print(f'A soma dos números é {somar}')
    elif opcão == 2:
        multiplicar = num1 * num2
        print(f'A multiplicação dos números é {multiplicar}')
    elif opcão == 3:
        if num1 > num2:
            print(f'O maior é: {num1}')
        else:
            print(f'O maior é: {num2}')
    elif opcão == 4:
        print('Informe os números novamente.')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        sleep(1)
        print(f'''{cores["Yellow"]}  -- Menu de opcões --
    {cores["Pink"]}[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcão = int(input(f'{cores["Yellow"]}Escoha uma opcão novamente: {cores["White"]}'))
print(f'Finalizando...')
sleep(2)
print(f'{cores["Red"]}PROGRAMA FINALIZADO.')
