# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores da lista em ordem crescente.

listaNum = escolha = []

while (escolha != 'N'):
    num = int(input('\nDigite um número: '))
    if num in listaNum:
        print(f'O número {num} já existe na lista! Não será adicionado novamente!\n')
    else:
        listaNum.append(num)
    escolha = input('Você deseja adicionar mais números? [S/N] ').strip().upper()[0]

listaNum.sort()
print('Os valores inseridos na lista são: ', end='')
for valor in listaNum:
    print(f' --> {valor}', end='')
