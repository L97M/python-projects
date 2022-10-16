# Crie um programa onde o usuário possa digitar sete valores e cadastre-os em uma lista única que mantenha separados os valroes pares e ímpares.
# No final, mostre os valores e ímares em ordem crescente

listaNumeros = []

print('\nPrograma para listagem de números pares e ímpares...\n')

for c in range(0, 7):
    n = int(input(f'Informe o {c + 1}º número: '))
    if (c == 0):
        listaNumeros.append([n])
        listaNumeros.append([])
    else:
        if (n % 2 == 0):
            if (listaNumeros[0][0] % 2 == 0):
                listaNumeros[0].append(n)
            else:
                listaNumeros[1].append(n)
        else:
            if (listaNumeros[0][0] % 2 != 0):
                listaNumeros[0].append(n)
            else:
                listaNumeros[1].append(n)

print('\nListas separadas e ordenadas abaixo: \n')

listaNumeros[0].sort()
listaNumeros[1].sort()

if (listaNumeros[0][0] % 2 == 0):
    print(f'Lista de Pares: {listaNumeros[0]}')
    print(f'Lista de Ímpares: {listaNumeros[1]}\n')
else:
    print(f'Lista de Pares: {listaNumeros[1]}')
    print(f'Lista de Ímpares: {listaNumeros[0]}\n')

# OBS: Seria possível resolver esse exercício definindo a lista da seguinte forma:
# listaNumeros = [[], []]
# Com isso, bastaria validar se o número é par ou impar e adicionar no índice desejado