# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

verificaParenteses = []
expressaoMat = input('\nDigite uma expressão matemática: ')

for elemento in expressaoMat:
    if (elemento == '('):
        verificaParenteses.append('(')
    elif (elemento == ')'):
        if (len(verificaParenteses) > 0):
            verificaParenteses.pop()
        else:
            verificaParenteses.append(')')
            break

if (len(verificaParenteses) == 0):
    print('\nA expressão matemática é válida!\n')
else:
    print('\nA expressão matemática NÃO é válida!\n')
