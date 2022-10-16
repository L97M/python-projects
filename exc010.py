# Código para ler um em BRL e apresentar quantos USDs podem ser comprados com esse valor
# No momento, o Dólar está valendo R$ 5,13
brl = float(input('Digite um valor em reais: R$ '))
usd = brl / 5.13
print('{} reais equivalem a {:.2f} dólares'.format(brl, usd))