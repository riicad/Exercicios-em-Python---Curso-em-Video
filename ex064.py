parar = contar = soma = 0
cores = {'Yellow': '\033[1;33m',
         'White': '\033[m',
         'Red': '\033[1;31m'}
print(f'{cores["Yellow"]}Digite quantos números quiser. Para finalizar o programa digite {cores["Red"]}999')
while parar != 999:
    parar = int(input(f'{cores["White"]}Digite um Número: '))
    if parar != 999:
        contar += 1
        soma += parar
    else:
        print(f'Programa {cores["Red"]}FINALIZADO{cores["White"]}.')
print(f'Total de números digitados: {cores["Yellow"]}{contar}')
print(f'{cores["White"]}A soma de todos os números é: {cores["Yellow"]}{soma}')
