# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (int)
# O programa vai informar quantas cédulas de cada valor serão entregues (Considerando que o caixa possui cédulas de 50, 20, 10 e 1 real)

cedulas1 = cedulas10 = cedulas20 = cedulas50 = 0

valor_saque = int(input('\nInforme o valor que deseja sacar: R$ '))

cedulas50 = valor_saque // 50
resta = valor_saque % 50

print(f'Você receberá R$ {valor_saque:.2f} em', end = ' ')

if (cedulas50 > 0):
    print(f'{cedulas50} nota(s) de 50', end = ' ')
if (resta >= 20):
    cedulas20 = resta // 20
    resta %= 20
    if (cedulas20 > 0):
        print(f'{cedulas20} nota(s) de 20', end = ' ')
if (resta >= 10):
    cedulas10 = resta // 10
    resta %= 10
    if (cedulas10 > 0):
        print(f'{cedulas10} nota(s) de 10', end = ' ')
if (resta >= 1):
    cedulas1 = resta // 1
    if (cedulas1 > 0):
     print(f'{cedulas1} nota(s) de 1', end = ' ')

# print(f'Você receberá R$ {valor_saque:.2f} em {cedulas50} nota(s) de 50, {cedulas20} nota(s) de 20, {cedulas10} nota(s) de 10 e {cedulas1} nota(s) de 1 real')
