contador = primeiro = antes = fibonacci = 0
elementos = int(input('Quantos termos você quer? '))
while contador != elementos + 1:
    antes = primeiro
    primeiro = fibonacci
    contador += 1
    if contador == 1:
        primeiro = 1
        antes = primeiro - 1
    else:
        fibonacci = primeiro + antes
        print(fibonacci, end=' -> ')
print('FIM')
