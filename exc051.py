# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
p_termo = int(input('\nInforme o primeiro termo de uma progressão aritmética: '))
razao = int(input('Informe a razão dessa progressão aritmética: '))
print('\nOs 10 primeiros termos são estes:')
dec_termo = p_termo + (10 - 1) * razao
for pa in range(p_termo, dec_termo + razao, razao):
    print(pa, end = ' ')
