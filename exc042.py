# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
if (abs(r2 - r3) < r1 and r1 < r2 + r3):
    print('Os 3 comprimentos de reta informados PODEM gerar um triângulo!')
    if (r1 == r2 and r1 == r3):
        print('O triângulo formado é do tipo EQUILÁTERO!')
    elif (r1 == r2 or r1 == r3 or r2 == r3):
        print('O triângulo formado é do tipo ISÓSCELES!')
    else:
        print('O triângulo formado é do tipo ESCALENO!')
else:
    print('Os 3 comprimentos de reta informados NÂO PODEM gerar um triângulo!')