# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
if (abs(r2 - r3) < r1 and r1 < r2 + r3):
    print('Os 3 comprimentos de reta informados PODEM gerar um triângulo!')
else:
    print('Os 3 comprimentos de reta informados NÂO PODEM gerar um triângulo!')