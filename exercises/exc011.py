# Código para ler a largura e altura de uma parede, então, calcular sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
ar = l * a
qt = ar / 2
print('A área total parede é {}'.format(ar))
print('A quantidade de tinta necessária para pintá-la é {}'.format(qt))

