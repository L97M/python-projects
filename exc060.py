# Faça um programa que leia um número qualquer e mostre o seu fatorial

n = int(input('\nInforme um número inteiro qualquer: '))
c = n
orig_n = n
print('{}! = {} '.format(orig_n, orig_n), end = '')
while (c != 1):
    print('x {} '.format(orig_n - 1), end = '')
    n = n * (c - 1)
    c -= 1
    orig_n -= 1

print('= {}'.format(n))
