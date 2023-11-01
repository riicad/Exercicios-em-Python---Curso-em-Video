op = list()
cl = list()

expressão = str(input('Digite uma expressão: '))

for i in expressão:

    if i == '(':
        op.append(i)

    elif i == ')':
        cl.append(i)

if len(op) == len(cl):
    print('A expressão digitada é válida.')

else:
    print('A expressão está errada!')
