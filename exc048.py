# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
from itertools import count


print('Números ímpares no intervalo entre 1 e 500: ')
s = 0
count = 0
for c in range(1, 501, 2):
    if (c % 3 == 0):
        count += 1
        s += c
print('A soma de todos os {} valores é: {}'.format(count, s))
