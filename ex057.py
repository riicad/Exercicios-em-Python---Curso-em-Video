resposta = 'b'
while resposta not in 'MmFf':
    resposta = str(input('Digite seu sexo [M/F]: ')).strip()[0]
    if resposta not in 'MmFf':
        print('Resposta inválida, tente novamente.')
print('Resposta arquivada com sucesso.')
