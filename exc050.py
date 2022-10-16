# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
s = 0
count = 0
print('\n')
for c in range(1,7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if (n % 2 == 0):
        count += 1
        s += n
print('A soma do(s) {} número(s) pares é: {}'.format(count, s))