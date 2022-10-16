# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# Ao final, mostre a matriz na tela, com a formatação correta

listaMatriz = [[], [], []]
contador = 0

print('\nCriando uma matriz...\n')

while (contador < 3):
    for c in range(0, 3):
        listaMatriz[contador].append(input(f'Digite um número ({contador}, {c}): '))
    contador += 1

print('\nE a matriz ficou assim:\n')

print(f'[ {listaMatriz[0][0]} ][ {listaMatriz[0][1]} ][ {listaMatriz[0][2]} ]')
print(f'[ {listaMatriz[1][0]} ][ {listaMatriz[1][1]} ][ {listaMatriz[1][2]} ]')
print(f'[ {listaMatriz[2][0]} ][ {listaMatriz[2][1]} ][ {listaMatriz[2][2]} ]')
