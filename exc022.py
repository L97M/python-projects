# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Qantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ').strip()
print('Nome Maiúsculo: {}'.format(nome.upper()))
print('Nome Minúsculo: {}'.format(nome.lower()))
# print('Nº total de letras (sem espaço): {}'.format(len(nome.replace(' ', ''))))
print('Nº total de letras (sem espaço): {}'.format(len(nome) - nome.count(' ')))
print('Nº de Letras do primeiro nome: {}'.format(len(nome.split()[0])))
