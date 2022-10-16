# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

print('\n')
for valor in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

menorValor = min(lista)
maiorValor = max(lista)

print(f'\nMenor valor: {menorValor}')
print(f'Ele aparece na(s) posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == menorValor:
        print(f'--> {i}', end=' ')
print()

print(f'\nMaior valor: {maiorValor}')

print(f'Ele aparece na(s) posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == maiorValor:
        print(f'--> {i}', end=' ')
print()