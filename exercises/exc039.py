# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano_atual = date.today()
sexo = input('Informe o seu sexo: ').strip().lower()
if (sexo == 'masculino'):
    idade = int(input('Informe a sua idade: '))
    if (idade > 17):
        ano_alistamento = ano_atual.year - (idade - 17)
        print('Você já passou da idade para alistamento!')
        print('O ano do seu alistamento era {}. Você está {} anos atrasado!'.format(ano_alistamento, ano_atual.year - ano_alistamento))
    elif (idade == 17):
        print('Parabéns! Você está apto a fazer o alistamento este ano!')
    else:
        ano_alistamento = 17 - idade
        print('Você não pode alistar-se no momento!')
        print('Você ainda precisa aguardar {} ano(s) para o seu alistamento, que será em {}!'.format(ano_alistamento, ano_atual.year + ano_alistamento))
else:
    print('Você não precisa fazer o alistamento obrigatório!')