# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

jogarDado = {}
contador = 1

for j in range(0, 4):
    jogarDado[f'jogador {j + 1}'] = randint(1, 6)

print('\nOs valores sorteados são: ')
for k, v in jogarDado.items():
    print(f'O {k} tirou {v}')

jogarDadoOrdenado = {k: v for k, v in sorted(jogarDado.items(), key=lambda item: item[1], reverse = True)}

print('\nRanking dos jogadores: ')
for k, v in jogarDadoOrdenado.items():
    print(f'{contador}º lugar: {k} com {v}')
    contador += 1
