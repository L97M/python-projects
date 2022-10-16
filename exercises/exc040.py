# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
n1 = float(input('Informe a sua nota 1: '))
n2 = float(input('Informe a sua nota 2: '))
m = (n1 + n2) / 2
if (m < 5):
    print('Você REPROVOU! Sua média foi {}!'.format(m))
elif (m >= 5 and m < 7):
    print('Você ficou em RECUPERAÇÃO! Sua média foi {}!'.format(m))
else:
    print('Você foi APROVADO! Sua média foi {}!'.format(m))