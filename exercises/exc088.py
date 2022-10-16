# Faça um programa que ajude um jogador da mega sena criar palpites
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# Todos os jogos devem ser cadastrados em uma lista composta

from random import randint
from time import sleep

listaJogos = []
cont = 0

print('\nFacilitador da MEGA SENA :D')
numJogos = int(input('\nQuantos jogos você deseja sortear? '))

for c in range(0, numJogos):
    listaJogos.append([])

while (cont < numJogos):
    for c in range(0, 6):
        randomNum = randint(1, 60)
        while (randomNum in listaJogos[cont]):
            randomNum = randint(1, 60)
        listaJogos[cont].append(randomNum)
    cont += 1

for c in range(0, numJogos):
    sleep(1)
    print(f'{c + 1}º jogo: {sorted(listaJogos[c])}')
