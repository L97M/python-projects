# Código para ler uma temperatura em graus °C e apresentar essa temperatura em °F
temp_cels = float(input('Informe a temperatura em °C: '))
temp_fahr = (temp_cels * 9 / 5) + 32
print('A temperatura {:.2f} °C equivale à {:.2f} °F'.format(temp_cels, temp_fahr))