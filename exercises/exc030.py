# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
n = int(input('Digite um número inteiro: '))
is_par = n % 2
print('Resto da divisão por 2: {}'.format(is_par))
if (is_par == 0):
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é IMPAR'.format(n))