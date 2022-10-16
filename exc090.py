# Faça um programa que leia nome e média de um aluno, assim como a sua situação (>= 7 aprovado)
# Salve tudo isso em um dicionário e apresente o conteúdo na tela

aluno = {}

nome = input('\nInforme o nome do(a) aluno(a): ')
media = float(input(f'Informe a média de {nome}: '))

aluno['nome'] = nome
aluno['media'] = media

if (media >= 7):
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(f'\nO nome do(a) aluno(a) é: {aluno["nome"]}')
print(f'A média de {aluno["nome"]} é: {aluno["media"]}')
print(f'A situação de {aluno["nome"]} é: {aluno["situacao"]}')
