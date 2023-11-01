from random import sample
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto aluno: ')
R = sample((A1, A2, A3, A4), k=4)
print('A ordem dos alunos sorteados é: \n{}'.format(R))
