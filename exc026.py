# Faça um programa que leia uma frase pelo teclado e mestre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
f = input('Digite uma frase: ').strip()
print('A letra "A" aparece {} vezes'.format(f.lower().count('a')))
print('O índice da sua primeira aparição é: {}'.format(f.lower().find('a') + 1))
print('O índice da sua última aparição é: {}'.format(f.lower().rfind('a') + 1))