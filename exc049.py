# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, usando o laço for
num = int(input('\nVocê deseja consultar a tabuada de qual número? '))
for c in range(1, 11):
    print('{:2} x {} = {:2}'.format(c, num, c * num))
