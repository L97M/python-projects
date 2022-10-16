# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA e mostrando os 10 primeiros termos da progressão
# Dessa vez, use a estrutura WHILE

c = 0
p_termo = int(input('\nInforme o primeiro termo da progressão aritmética: '))
rz = int(input('Informe a razão dessa progressão: '))

while (c < 10):
    print(p_termo, end = ' ')
    p_termo += rz
    c += 1