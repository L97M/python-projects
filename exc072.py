# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero à vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

num = 0
escolha = []
numExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
                'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
                'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
                'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while (escolha != 'N'):
    while True:
        num = int(input('\nInforme um número (0 à 20): '))
        if (num >= 0 and num <= 20):
            break
        print('Número inválido! Tente novamente!')
    print(f'Número digitado: {numExtenso[num]}\n')
    escolha = input('Você deseja informar outro número? [N] Não [Qualquer tecla] Sim.. ').strip().upper()
