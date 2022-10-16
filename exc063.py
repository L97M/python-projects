# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência Fibonacci

n = int(input('\nQuantos termos você quer mostrar? '))
p_termo = 0
s_termo = 1
fn = 0
c = 2

print('0 1', end = ' ')
while (c < n):
    fn = p_termo + s_termo
    print(fn, end = ' ')
    p_termo = s_termo
    s_termo = fn
    c += 1