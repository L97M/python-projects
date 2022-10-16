# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = s = n_qtd = 0
while (True):
    n = int(input('\nInforme um número (999 para encerrar): '))
    if (n == 999):
        break
    s += n
    n_qtd += 1
print(f'\nForam digitados {n_qtd} números e a soma entre eles vale {s}!\n')
