# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
f = input('\nDigite uma frase qualquer: ').strip().lower()
replacef = f.replace(' ','')
if (replacef == replacef[::-1]):
    print('A frase "{}" É um palíndromo!'.format(f))
else:
    print('A frase "{}" NÂO é um palíndromo!'.format(f))
