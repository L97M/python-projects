# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços organizando os dados em tabular

c = 0
tuplaListaPrecos = ('Arroz', 5, 'Feijão', 4, 'Salada', 2, 'Bebida', 3, 'Carne', 7, 'Sobremesa', 2)

print('-' * 35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-' * 35)

while (c < len(tuplaListaPrecos)):
    print(f'{tuplaListaPrecos[c]:.<30}', end = '')
    print(f'R$ {tuplaListaPrecos[c + 1]:>5.2f}')
    c += 2
