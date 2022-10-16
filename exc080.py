# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

listaNum = []
pos = 0

for c in range(0, 5):
    num = int(input('\nDigite um número: '))
    if (c == 0 or num > listaNum[len(listaNum) - 1]):
        listaNum.append(num)
        print('Valor adicionado ao final da lista...')
    elif (num < listaNum[0]):
        listaNum.insert(0, num)
        print('Valor adicionado ao início da lista...')
    elif (num in listaNum):
        listaNum.insert(listaNum.index(num), num)
        print('Valor adicionado ao meio da lista...')
    else:
        for cont in range(0, len(listaNum)):
            if (num > listaNum[cont]):
                pos = listaNum.index(listaNum[cont]) + 1
        listaNum.insert(pos, num)
        print('Valor adicionado ao meio da lista...')
print(f'\nLista ordenada: {listaNum}\n')
