# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0.5 por Km para viagens de até 200 Km e R$ 0.45 para viagens mais longas
km = float(input('Informe a distância da viagem em Km: '))
if (km <= 200):
    print('A sua viagem terá o valor de R$ {:.2f}'.format(km * 0.5))
else:
    print('A sua viagem terá o valor de R$ {:.2f}'.format(km * 0.45))