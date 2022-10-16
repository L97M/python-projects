# Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
jokenpo_pc_lista = ['pedra', 'papel', 'tesoura']
mao_jogador = input('Jo... Ken... Pô..?! ').strip().lower()
mao_pc = choice(jokenpo_pc_lista)
if (mao_pc == mao_jogador):
    print('EMPATE! Tente novamente!')
elif(mao_jogador == 'tesoura' and mao_pc == 'papel'):
    print('O jogador VENCEU! Tesoura corta o papel.')
elif (mao_jogador == 'tesoura' and mao_pc == 'pedra'):
    print('O jogador PERDEU! Pedra quebra a tesoura.')
elif (mao_jogador == 'papel' and mao_pc == 'tesoura'):
    print('O jogador PERDEU! Tesoura corta o papel.')
elif (mao_jogador == 'papel' and mao_pc == 'pedra'):
    print('O jogador VENCEU! Papel embrulha a pedra.')
elif (mao_jogador == 'pedra' and mao_pc == 'tesoura'):
    print('O jogador VENCEU! Pedra quebra a tesoura.')
elif (mao_jogador == 'pedra' and mao_pc == 'papel'):
    print('O jogador PERDEU! Papel embrulha a pedra.')