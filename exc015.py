# Código para perguntar a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado
alug_dias = int(input('Quantos dias de aluguel? '))
alug_km = float(input('Quantos KMs foram rodados? '))
valor_final = 60 * alug_dias + 0.15 * alug_km
print('Total a pagar: R$ {:.2f}'.format(valor_final))