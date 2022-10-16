# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

from time import sleep

listaMatriz = [[], [], []]
somaPar = 0

print('\nCriando uma matriz...\n')

for c in range(0, 3):
    n = int(input(f'Digite um número (0, {c}): '))
    listaMatriz[0].append(n)
    if (n % 2 == 0):
        somaPar += n

for c in range(0, 3):
    n = int(input(f'Digite um número (1, {c}): '))
    listaMatriz[1].append(n)
    if (n % 2 == 0):
        somaPar += n

for c in range(0, 3):
    n = int(input(f'Digite um número (2, {c}): '))
    listaMatriz[2].append(n)
    if (n % 2 == 0):
        somaPar += n

print('\nE a matriz ficou assim:\n')

print(f'[ {listaMatriz[0][0]} ][ {listaMatriz[0][1]} ][ {listaMatriz[0][2]} ]')
print(f'[ {listaMatriz[1][0]} ][ {listaMatriz[1][1]} ][ {listaMatriz[1][2]} ]')
print(f'[ {listaMatriz[2][0]} ][ {listaMatriz[2][1]} ][ {listaMatriz[2][2]} ]')

print('\nGerando o relatório...\n')
sleep(1)

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da 3ª coluna é {listaMatriz[0][2] + listaMatriz[1][2] + listaMatriz[2][2]}')

if (listaMatriz[1][0] > listaMatriz[1][1] > listaMatriz[1][2]):
    print(f'O maior valor da 2ª linha é {listaMatriz[1][0]}\n')
elif (listaMatriz[1][1] > listaMatriz[1][0] > listaMatriz[1][2]):
    print(f'O maior valor da 2ª linha é {listaMatriz[1][1]}\n')
else:
    print(f'O maior valor da 2ª linha é {listaMatriz[1][2]}\n')
    