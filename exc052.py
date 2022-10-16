# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
# Lógica usada:  nºs primos são números naturais divisíveis apenas por 1 e si próprio.
n = int(input('\nInforme um número inteiro qualquer: '))
count = 0
for d in range(1, n + 1):
    if (n % d == 0):
        count += 1
if (count > 2 or n == 1):
    print('O número {} NÃO é primo!'.format(n))
else:
    print('O número {} É primo!'.format(n))


    
