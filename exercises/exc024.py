# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
c = input('Digite o nome de uma cidade: ').lower().strip().split()
print('santo' in c[0])
