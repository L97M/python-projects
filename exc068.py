# Faça um programa que jogue par ou ímpar com o computador
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias e consecutivas que ele conseguiu

from random import randint

cont_vitorias = 0

while True:
    num_pc = randint(0, 10)
    par_ou_impar = input('\nVocê quer PAR ou ÍMPAR? ').strip().upper()[0]
    if (par_ou_impar == 'P'):
        num_player = int(input('\nInforme um número entre 0 e 10: '))
        result = num_pc + num_player
        if (result % 2 == 0):
            print(f'Você VENCEU! O PC jogou {num_pc} e soma dos valores é {result}, que é um número PAR!')
            cont_vitorias += 1
        else:
            print(f'Você PERDEU! O PC jogou {num_pc} e soma dos valores é {result}, que é um número ÍMPAR!')
            break
    elif (par_ou_impar == 'I' or par_ou_impar == 'Í'):
        num_player = int(input('\nInforme um número entre 0 e 10: '))
        result = num_pc + num_player
        if (result % 2 != 0):
            print(f'Você VENCEU! O PC jogou {num_pc} e soma dos valores é {result}, que é um número ÍMPAR!')
            cont_vitorias += 1
        else:
            print(f'Você PERDEU! O PC jogou {num_pc} e soma dos valores é {result}, que é um número PAR!')
            break
    else:
        print('\nOpção inválida! Tente novamente: ')

print(f'\nNo total, você venceu {cont_vitorias} vezes.')
