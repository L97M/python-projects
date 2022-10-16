# Faça um programa que leia 3 números e mostre qual é o maior e o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if (n1 > n2 and n1 > n3):
    print('{} é o MAIOR número!'.format(n1))
elif (n2 > n1 and n2 > n3):
    print('{} é o MAIOR número!'.format(n2))
else:
    print('{} é o MAIOR número!'.format(n3))

if (n1 < n2 and n1 < n3):
    print('{} é o MENOR número!'.format(n1))
elif (n2 < n1 and n2 < n3):
    print('{} é o MENOR número!'.format(n2))
else:
    print('{} é o MENOR número!'.format(n3))
