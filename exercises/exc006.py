# Código para ler um número e apresentar o seu dobro, triplo e raiz quadrada
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
# print('O dobro de {} é {}'.format(n, d))
# print('O triplo de {} é {}'.format(n, t))
# print('A raiz quadrada de {} é {:.3f}'.format(n, rq))
print('O dobro de {} é {} \nO triplo de {} é {}\nA raiz quadrada de {} é {:.3f}'.format(n, d, n, t, n, rq))
# Lembrando que os cálculos tbm podem ser feitos dentro dos formats e a raiz quadrada tem a função pow dedicada pra isso
