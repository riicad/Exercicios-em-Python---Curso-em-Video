cont = mais = total = 0
cores = {'y': '\033[1;33m',
         'r': '\033[1;31m',
         'w': '\033[m'}
print(f'{cores["y"]}--' * 15, f'\n{"Supermercado ATACADÃO": ^30}')
while True:
    print(f'{cores["y"]}--' * 15, f'{cores["w"]}')
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        mais += 1
    if cont == 1:
        menos = preço
        menor = nome
    if preço < menos:
        menos = preço
        menor = nome
    print(f'{cores["y"]}--' * 15, f'{cores["w"]}')
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f"{cores['r']}{'PROGRAMA FINALIZADO':-^30}{cores['w']}")
print(f'''Total gasto: R${cores["y"]}{total:.2f}
{cores["w"]}Quantidade de produtos que custam mais de R$1000: {cores["y"]}{mais}
{cores["w"]}O nome do menor produto é {cores["y"]}{menor.upper()}{cores["w"]}. Ele custa R${cores["y"]}{menos:.2f}''')
