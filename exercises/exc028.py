# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 r 5 e peça para o usuário tentar descobrir qual o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
n = randint(0,5)
user_n = int(input('Informe um número de 0 à 5: '))
if (n == user_n):
    print('Você venceu! Parabéns!')
else:
    print('Você perdeu! O número era {}!'.format(n))