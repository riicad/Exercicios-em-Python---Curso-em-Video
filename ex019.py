import random
A1 = str(input('Nome do primeiro aluno: '))
A2 = str(input('Nome do segundo aluno: '))
A3 = str(input('Nome do terceiro aluno: '))
A4 = str(input('Nome do quarto aluno: '))
lista = (A1, A2, A3, A4)
c = random.choice(lista)
print('O garoto sorteado é: {}'.format(c))



