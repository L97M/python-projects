# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o número solicitado for negativo

while True:
    num = int(input('\nQual tabuada você deseja verificar? '))
    # if (num <= num - (num + 1)):
    if (num < 0):
        print("\nVocê digitou um número negativo... Saindo do programa!")
        break
    else:
        # cont = 1
        # while (cont < 11):
        for cont in range(1, 11):
            print(f'{num} x {cont:2} = {num * cont:2}')
            # cont += 1
