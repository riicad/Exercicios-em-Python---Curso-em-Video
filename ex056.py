cores = {'White': '\033[m',
         'Green': '\033[1;32m'}
zero = 0
y = [0, 1, 2, 3, 4]
n = [0, 1, 2, 3, 4]
s = [0, 1, 2, 3, 4]
for i in range(1, 5):
    print(f'-=-=-=- {cores["Green"]}{i}° PESSOA{cores["White"]} -=-=-=-')
    nome = str(input(f'Digite seu nome: ')).strip()
    idad = int(input(f'Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: ')).lower().stri()
    y[i] = idad
    s[i] = sexo
    n[i] = nome
    if s[i] == 'masculino' and y[i] == max(y):
        véi = n[i]
    elif s[i] == 'feminino' and y[i] < 20:
        zero += 1
média = (y[1] + y[2] + y[3] + y[4])/4
print(f'A média da idade dessas pessoas é: {média} anos.')
print(f'O nome do homem mais vélho é: {véi}')
print(f'A quantidade de mulheres com menos de 20 anos é: {zero}')

