# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores
from datetime import date
ano_atual = date.today().year
menores = 0
maiores = 0
print('\n')
for p in range(0, 7):
    an = int(input('Ano de nascimento {}: '.format(p + 1)))
    if (ano_atual - an < 18):
        menores += 1
    else:
        maiores += 1
print('\n{} pessoas já são maiores de idade. Enquanto, {} ainda são menores.'.format(maiores, menores))
