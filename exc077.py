# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

tuplaPalavras = ('Carro', 'Arvore', 'Casa', 'Onibus', 'Ventilador',
                'Monitor', 'Computador', 'Dinheiro', 'Aluguel')

for palavra in tuplaPalavras:
    print(f'\nNa palavra {palavra} temos ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end = ' ')
