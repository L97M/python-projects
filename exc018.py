# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan
ang = float(input('Informe um ângulo qualquer: '))
ang_rad = ang * 3.14 / 180
print('O Seno de {} é {:.2f}\nO Cosseno é {:.2f}\nA Tangente é {:.2f}'.format(ang, sin(ang_rad), cos(ang_rad), tan(ang_rad)))
