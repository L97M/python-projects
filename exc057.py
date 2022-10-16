# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peça a digitação novamente até ter um valor correto

p_sexo = input('\nInforme o seu sexo [M/F]: ').strip().upper()

while (p_sexo != 'M' and p_sexo != 'F'):
    print('\nSexo não identificado. Tente novamente, por favor!')
    p_sexo = input('\nInforme o seu sexo [M/F]: ')

print('\nSexo cadastrado com sucesso!')





