# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
num = int(input('Informe um número inteiro qualquer: '))
escolha = int(input('Você deseja converter o número informado para qual base? [1] Binário [2] Octal [3] Hexadecimal: '))
if (escolha == 1):
    print('O valor {} convertido para Binário é {}!'.format(num, bin(num)[2:]))
elif (escolha == 2):
    print('O valor {} convertido para Octal é {}!'.format(num, oct(num)[2:]))
elif (escolha == 3):
    print('O valor {} convertido para Hexadecimal é {}!'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
