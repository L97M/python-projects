# Melhore o jogo do DESAFIO 028, onde o computador vai pensar em um número entre 0 e 10
# Agora o jogador deve tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint

tentativas = 1
pc_num = randint(0, 10)
jogador_num = int(input('\nInforme um número de 0 a 10: '))

while (jogador_num != pc_num):
    print('\nVocê errou! Tente novamente!')
    if (pc_num > jogador_num):
        print('\nO valor é MAIOR...')
    else:
        print('\nO valor é MENOR...')
    jogador_num = int(input('\nInforme um número de 0 a 10: '))
    tentativas += 1

print('\nParabéns! Você acertou na {}ª tentativa.'.format(tentativas))
