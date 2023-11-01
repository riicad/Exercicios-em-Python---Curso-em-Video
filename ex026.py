frase = str(input('Diga-me uma frase: ')).strip()
Acima = frase.upper()
A = Acima.count('A')
print('A quantidade de "A" na sua frase é: {}'.format(A))
Primeira = Acima.find('A') + 1
print('A primeira letra "A" aparece em {}'.format(Primeira))
Ultima = Acima.rfind('A') + 1
print('A útilma letra "A" aparece em {}'.format(Ultima))
