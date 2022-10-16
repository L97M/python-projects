# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado
valor_casa = float(input('Informe o valor da casa desejada: R$ '))
sal_comprador = float(input('Informe o seu salário mensal: R$ '))
qtd_anos_pgmt = int(input('Informe em quantos anos irá pagar: '))
prestacao = valor_casa / (qtd_anos_pgmt * 12)
if (prestacao > sal_comprador * 30 / 100):
    print("O valor das parcelas excede 30% do seu salário. Empréstimo NÂO aprovado!")
else:
    print("Empréstimo aprovado! A prestação mensal será de R$ {:.2f}! Parabéns pela casa nova!".format(prestacao))