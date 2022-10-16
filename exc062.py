# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa deve encerrar quando ele disser que quer mostrar 0 termos

c = 0
opc = []
p_termo = int(input('\nInforme o primeiro termo de uma progressão aritmética: '))
rz = int(input('Ok! E qual a razão dessa progressão? '))

print('\nOs 10 primeiros termos dessa progressão são estes: ')
while (c < 10):
    print(p_termo, end = ' ')
    p_termo += rz
    c += 1

while (opc != 'N'):
    opc = input('\n\nVocê deseja analisar mais alguns termos da progressão? [S/N] ').strip().upper()
    if (opc == 'S'):
        n_qtd = int(input('\nMais quantos termos você deseja verificar? '))
        print('\nCerto! Os próximos {} termos são: '.format(n_qtd))
        n_qtd += c
        while (c < n_qtd):
            print(p_termo, end = ' ')
            p_termo += rz
            c += 1
    elif (opc == 'N'):
        print('\nOk! Foram verificados {} termos da progressão aritmética!\nAté mais!'.format(c))
    else:
        print('\nOpção inválida! Tente novamente, por favor!')
