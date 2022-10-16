# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
if (num1 > num2):
    print('O número {} é maior que o número {}!'.format(num1, num2))
elif (num2 > num1):
    print('O número {} é maior que o número {}!'.format(num2, num1))
else: 
    print('O número {} é igual ao número {}!'.format(num1, num2))