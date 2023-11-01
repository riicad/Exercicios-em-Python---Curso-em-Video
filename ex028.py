from random import randint
from time import sleep
print("Pensando em número de 0 a 5.")
PC = randint(0, 5)
print('Aguarde...\nAguarde...\nPronto!')
sleep(3)
Sorte = int(input('Em que número eu pensei? '))
print('CORRETO!\nPARABÉNS!!!\nVOCÊ ACERTOU!' if PC == Sorte else 'Que pena..\nA resposta esta incorreta.')







