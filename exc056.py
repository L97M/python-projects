# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

m_idades = 0
h_maior_idade = 0
h_nome = []
mlhrs_idade = 0
for p in range(1, 5):
    p_nome = input('\nInforme o nome da {}ª pessoa: '.format(p))
    p_idade = int(input('Informe a idade da {}º pessoa: '.format(p)))
    p_sexo = input('Informe o sexo da {}º pessoa [m/f]: '.format(p)).strip().lower()
    m_idades += p_idade
    if (p == 1 and p_sexo == 'm'):
        h_maior_idade = p_idade
        h_nome = p_nome
    if (p_sexo == 'm' and p_idade > h_maior_idade):
        h_maior_idade = p_idade
        h_nome = p_nome
    if (p_sexo == 'f' and p_idade > 20):
        mlhrs_idade += 1

m_idades = m_idades / 4
print('\nA média das idades é: {}!'.format(m_idades))
print('O homem mais velho tem {} anos e chama-se {}!'.format(h_maior_idade, h_nome))
print('Ao todo, {} mulher(es) tem(êm) menos de 20 anos!'.format(mlhrs_idade))
