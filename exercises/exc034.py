# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para salários os inferiores, o aumento é de 15%
sal = float(input('Informe o seu salário atual: R$ '))
if (sal > 1250):
    aument = sal * 10 / 100
    nv_sal = sal + aument
    print('Seu salário terá um aumento de {:.2f} e ficará {:.2f}'.format(aument, nv_sal))
else:
    aument = sal * 15 / 100
    nv_sal = sal + aument
    print('Seu salário terá um aumento de {:.2f} e ficará {:.2f}'.format(aument, nv_sal))