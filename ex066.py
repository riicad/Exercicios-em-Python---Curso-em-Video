cores = {'y': '\033[1;33m',
         'w': '\033[m'}
s = d = int()
while True:
    número = int(input('Digite um número (999 faz parar): '))
    if número == 999:
        break
    s += número
    d += 1
print(f'''A quantidade de números digitados é: {cores["y"]}{d}
{cores["w"]}A soma dos números digitados é: {cores["y"]}{s}''')
