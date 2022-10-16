# Código para ler um número inteiro e apresentar o seu sucessor e antecessor
num = int(input('Digite um número: '))
print('O antecessor de {} é {}'.format(num, num - 1))
print('O sucessor de {} é {}'.format(num, num + 1))