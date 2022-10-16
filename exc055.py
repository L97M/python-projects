# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
menor_p = 0
maior_p = 0
print('\n')
for p in range(0, 5):
    peso = float(input('Informe o peso da {}º pessoa: '.format(p + 1)))
    if (p == 1):
        maior_p = peso
        menor_p = peso
    else:
        if (peso > maior_p):
            maior_p = peso
        if (peso < menor_p):
            menor_p = peso
print('\nO maior peso informado foi: {}Kg! Já o menor peso foi: {}Kg\n'.format(maior_p, menor_p))
