# Código para ler um valor e apresentar o valor - 5%
pr = float(input('Digite o preço do produto: R$ '))
desc = 5 / 100 * pr
n_pr = pr - desc
print('O valor do produto com desconto de 5% ({:.2f}) é R$ {:.2f}'.format(desc, n_pr))