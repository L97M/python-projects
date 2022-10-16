# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista (dinheiro/cheque): 10% off
# À vista no cartão: 5% off
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
pp = float(input('Informe o valor base do produto: R$ '))
fp = int(input('\nOpções de pagamento: \n[1] À vista (dinheiro ou cheque) \n[2] À vista (cartão) \n[3] Até 2x no cartão \n[4] 3x ou mais no cartão \n\nComo fica melhor para você? '))
if (fp == 1):
    print('Nessa forma de pagamento você ganha 10% de desconto! O valor ficará R$ {}!'.format(pp - pp * 10 / 100))
elif (fp == 2):
    print('Nessa forma de pagamento você ganha 5% de desconto! O valor ficará R$ {}!'.format(pp - pp * 5 / 100))
elif (fp == 3):
    print('Nessa forma de pagamento você ganha 2% de desconto! O valor ficará R$ {}!'.format(pp - pp * 2 / 100))
elif (fp == 4):
    print('Nessa forma de pagamento o valor recebe 20% de juros! No total ficará R$ {}!'.format(pp + pp * 20 / 100))
else:
    print('Opção inválida! Tente novamente!')