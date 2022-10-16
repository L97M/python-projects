# Código para ler um valor em metros e converter em centímetros e milímetros
n = float(input('Digite um número em metros: '))
cent = n * 100
milim = n * 1000
print('{} em centímetros é {}'.format(n, cent))
print('{} em milímetros é {}'.format(n, milim))