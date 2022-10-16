# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 20 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
p = float(input('Informe seu peso: '))
a = float(input('Informe a sua altura: '))
imc = p / a ** 2
if (imc < 18.5):
    print('Você está ABAIXO do peso ideal!')
elif (imc >= 18.5 and imc <= 25):
    print('Você está no PESO IDEAL! Parabéns!')
elif (imc > 25 and imc <= 30):
    print('Você está ACIMA do peso ideal!')
elif (imc > 30 and imc <= 40):
    print('Você está OBESO! Cuidado!')
else:
    print('Você atingiu a OBESIDADE MÓRBIDA!')
