# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre na tela a média entre todos valores e qual foi o maior e o menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

opc = []
c = aux = n_maior = n_menor = 0

while (opc != 'N'):
    n = int(input('\nInforme um número inteiro qualquer: '))
    if (c == 1):
        n_maior = n
        n_menor = n
    elif (n > n_maior):
        n_maior = n
    elif (n < n_menor):
        n_menor = n
    c += 1
    aux += n
    opc = input('\nDeseja informar mais algum número?\nPressione [qualquer tecla] para CONTINUAR ou [N] para SAIR: ').strip().upper()

print('\nA média entre os valores digitados foi {:.2f}!'.format(aux / c))
print('O maior número foi o {}. Já o menor, foi {}'.format(n_maior, n_menor))
