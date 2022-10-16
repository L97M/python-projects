# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

p_maiores = p_homens = p_mulheres = 0

while True:
    p_idade = int(input('\nInforme a idade: '))
    p_sexo = input('Informe o sexo: ').strip().upper()[0]
    if (p_sexo == 'M'):
        p_homens += 1
    elif (p_sexo == 'F' or p_sexo == 'F' and p_idade < 20):
        # if (p_idade < 20):
        p_mulheres += 1
    else:
        print('\nSexo não encontrado! Tente novamente!')
    if (p_idade > 17):
        p_maiores += 1
    escolha = input('\nVocê deseja cadastrar mais pessoas? [N] para sair ou [Qualquer tecla] para continuar.. ').strip().upper()
    if (escolha == 'N'):
        print('\nOk! Gerando o relatório...')
        break

print(f'\nAo todo, foi feito o cadastro de {p_homens} homem(ns).\n{p_maiores} pessoa(s) é(são) maior(es) de idade.\n{p_mulheres} mulher(es) tem menos de 20 anos.')