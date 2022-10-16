# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

# dicDado = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
dicDado = {}

for j in range(0, 4):
    dicDado[f'jogador{j + 1}'] = randint(1, 6)