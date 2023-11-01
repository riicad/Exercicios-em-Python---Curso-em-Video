from datetime import date

pessoa = dict()

pessoa["Nome"] = str(input('Nome: '))

an = int(input('Data de nascimento: '))
pessoa["Idade"] = date.today().year - an

pessoa["CTPS"] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa["CTPS"] != 0:

    pessoa["Contratação"] = int(input('Ano de contratação: '))
    pessoa["Salário"] = float(input('Salário: R$'))

    ap = date.today().year - pessoa["Contratação"]
    pessoa["Aposentadoria"] = pessoa["Idade"] + (35 - ap)

print('-='*20)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
