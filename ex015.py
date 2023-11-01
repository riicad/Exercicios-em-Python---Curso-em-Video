k = float(input('Quantos km o carro percorreu? '))
d = int(input('Quantos dias ele foi alugado? '))
s = d*60
m = k*0.15
t = s + m
print('O preço a pagar por esse carro vai ser: R${:.2f}'.format(t))

