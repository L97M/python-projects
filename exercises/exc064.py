# Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag

n = n_qtd = n_soma = 0

while (n != 999):
        n_soma += n
        n_qtd += 1
        n = int(input('\nInforme um número inteiro qualquer ou 999 para encerrar o programa: '))

print('\nAo todo, foram carregados {} números e a soma entre eles é {}'.format(n_qtd - 1, n_soma))
