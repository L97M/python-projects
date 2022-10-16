# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3 (informar se o valor não apareceu)
# Quais foram os números pares

n1 = int(input('\nInforme um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
n3 = int(input('Informe mais um número inteiro: '))
n4 = int(input('Informe o último número inteiro: '))

tuplaNum = (n1, n2, n3, n4)

print(f'\nO número 9 apareceu {tuplaNum.count(9)} vezes!')

if 3 in tuplaNum:
    print(f'O número 3 apareceu na {tuplaNum.index(3) + 1}ª posição!')
else:
    print('O número 3 não foi digitado!')

# if (tuplaNum.count(3) == 0):
#     print('O número 3 não foi digitado!')
# else:
#     print(f'O número 3 apareceu na {tuplaNum.index(3) + 1}ª posição!')

print('Números pares:', end = ' ')
for num in tuplaNum:
    if (num % 2 == 0):
        print(num, end = ' ')
