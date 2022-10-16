# Crie um programa que vai gerar 5 números aleatórios e colar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
from time import sleep

tuplaNum = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('\nSorteando números...\n')
sleep(1.5)

for num in tuplaNum:
    print(num, end = ' ')

# sortedTuplaNum = sorted(tuplaNum)
# print(f'\n\nMenor número sorteado: {sortedTuplaNum[0]}')
# print(f'Maior número sorteado: {sortedTuplaNum[4]}\n')

print(f'\n\nMenor número sorteado: {max(tuplaNum)}')
print(f'Menor número sorteado: {min(tuplaNum)}')
