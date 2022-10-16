# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
vel = int(input('Informe a velocidade do carro em km/h: '))
if (vel > 80):
    exc_vel = (vel - 80) * 7
    print('Você excedeu o limite de velocidade e foi multado!\nA multa vai custar R$ {}'.format(exc_vel))
else:
    print('Você está dentro do limite de velocidade. Boa viagem!')