aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'

else:
    aluno['Situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'-- {k} é igual a {v}')

