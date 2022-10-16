# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

opc = 0

n1 = int(input('\nInforme o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

print('\nAções disponíveis para processamento:')

while (opc != 5):
    print('''\nEscolha uma das opções abaixo ou digite 5 para sair.\n
    # [1] somar
    # [2] multiplicar
    # [3] maior
    # [4] novos números
    # [5] sair do programa''')

    opc = int(input('\nInforme a opção desejada: '))

    if (opc == 1):
        print('\nA soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
    elif (opc == 2):
        print('\nA produto de {} e {} é: {}'.format(n1, n2, n1 * n2))
    elif (opc == 3):
        if (n1 > n2):
            print('\n{} é maior que {}'.format(n1, n2))
        elif (n2 > n1):
            print('\n{} é maior que {}'.format(n2, n1))
        else:
            print('\nOs valores digitados são iguais!')
    elif (opc == 4):
        n1 = int(input('\nOk, informe outro primeiro valor: '))
        n2 = int(input('Informe também outro segundo valor: '))
    elif (opc == 5):
        print('\nSaindo do programa. Até logo!')
    else:
        print('\nO valor digitado é inválido! Tente novamente!')
