# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contentando a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

listaAlunos = []
cont = 0

while True:
    nome = input('\nInforme o nome do(a) aluno(a): ')
    listaAlunos.append([nome])
    nota1 = float(input('Informe a 1ª nota do(a) aluno(a): '))
    listaAlunos[cont].append([nota1])
    nota2 = float(input('Informe a 2ª nota do(a) aluno(a): '))
    listaAlunos[cont][1].append(nota2)
    media = (nota1 + nota2) / 2
    listaAlunos[cont][1].append(media)
    opc = input('\nDeseja adicionais mais dados? [N] Sair [Qualquer tecla] Continuar ').upper().strip()
    if (opc == 'N'):
        print('\nOk! Gerando relatório...\n')
        break
    cont += 1

for c in range(len(listaAlunos)):
    print(f'{c}    {listaAlunos[c][0]}    {listaAlunos[c][1][2]}')

while True:
    continuar = input('\nDeseja verificar a nota de algum(a) aluno(a)? [N] Sair [Qualquer tecla] Continuar ').upper().strip()
    if (continuar == 'N'):
        print('\nOk! Saindo do programa...\n')
        break
    opc = int(input('\nMostrar notas de qual aluno(a)? '))
    print(f'\nNotas de {listaAlunos[opc][0]} são: {listaAlunos[opc][1][0]} e {listaAlunos[opc][1][1]}')