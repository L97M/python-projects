# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# b) A lista de valores ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista

listaNum = []

while True:
    listaNum.append(int(input('\nInforme um número: ')))
    escolha = input('Deseja adicionar mais números? [S/N] ').strip().upper()[0]
    if (escolha == 'N'):
        print('\nOk. Gerando relatório...')
        break

print(f'\nQuantidade de números digitados: {len(listaNum)}')

listaNum.sort(reverse=True)

print(f'Lista ordenada (decrescente): {listaNum}')

if 5 in listaNum:
    print('O valor 5 foi digitado!\n')
else:
    print('O valor 5 não foi digitado!\n')
