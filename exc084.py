# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas?
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maisPesados = []
nomeMaisPesados = []
nomeMaisLeves = []
maisLeves = []

while True:
    dados.append(input('\nInforme o nome da pessoa: '))
    dados.append(float(input('Informe o peso da pessoa (KG): ')))
    pessoas.append(dados[:])
    if (len(pessoas) == 1):
        maisPesados.append(dados[:])
        maisLeves.append(dados[:])
    else:
        if (dados[1] > maisPesados[0][1]):
            maisPesados.clear()
            maisPesados.append(dados[:])
        elif (dados[1] == maisPesados[0][1]):
            maisPesados.append(dados[:])
        elif (dados[1] < maisLeves[0][1]):
            maisLeves.clear()
            maisLeves.append(dados[:])
        elif (dados[1] == maisLeves[0][1]):
            maisLeves.append(dados[:])
    dados.clear()
    escolha = input('\nDeseja adicionar mais uma pessoa? [N] Sair [Qualquer tecla] Continuar... ').strip().upper()
    if (escolha == 'N'):
        print('\nOk. Gerando relatório...')
        break

print(f'\nForam cadastradas {len(pessoas)} pessoas')

if (len(maisPesados) > 1):
    for p in maisPesados:
        nomeMaisPesados.append(p[0])
    print(f'O maior peso foi de {maisPesados[0][1]}Kg. Peso de {nomeMaisPesados}')
else:
    print(f'O maior peso foi de {maisPesados[0][1]}Kg. Peso de {maisPesados[0][0]}')

if (len(maisLeves) > 1):
    for p in maisLeves:
        nomeMaisLeves.append(p[0])
    print(f'O menor peso foi de {maisLeves[0][1]}Kg. Peso de {nomeMaisLeves}\n')
else:
    print(f'O menor peso foi de {maisLeves[0][1]}Kg. Peso de {maisLeves[0][0]}\n')
