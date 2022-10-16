# Faça um programa que leia o nome de 4 alunos(as) e sorteie um deles
from random import choice
n1 = input('Informe o primeiro nome: ')
n2 = input('Informe o segundo nome: ')
n3 = input('Informe o terceiro nome: ')
n4 = input('Informe o quarto nome: ')
name_list = [n1, n2, n3, n4]
print('O(a) aluno(a) escolhido(a) é {}'.format(choice(name_list)))