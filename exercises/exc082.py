# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

listaNum = []
listaNumPares = []
listaNumImpares = []

while True:
    listaNum.append(int(input('\nInforme um número: ')))
    escolha = input('Deseja informar mais números? [S/N] ').strip().upper()[0]
    if (escolha == 'N'):
        print('\nOk. Analisando os dados...')
        break

for valor in listaNum:
    if (valor % 2 == 0):
        listaNumPares.append(valor)
    else:
        listaNumImpares.append(valor)

print(f'\nLista completa: {listaNum}')
print(f'Lista de pares: {listaNumPares}')
print(f'Lista de ímpares: {listaNumImpares}\n')
