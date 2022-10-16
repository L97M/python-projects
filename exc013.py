# Código para ler o valor de salário de um colaborar e informar o seu novo salário com base em 15% de aumento
sal = float(input('Informe o valor de salário: R$ '))
aum = sal + (sal * 15 / 100)
print('Com o aumento de 15%, o salário passou a ser R$ {:.2f}'.format(aum))