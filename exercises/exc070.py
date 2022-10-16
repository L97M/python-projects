# Crie um programa que leia o nome e o preço de vários produtos
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) qual é o total gasto na compra
# B) quantos produtos custam mais de 1000 reais
# c) qual é o nome do produto mais barato

p_barato = escolha = []
p_caro = valor_tot = cont = p_preco_aux = 0

while True:
    cont += 1
    p_nome = input('\nInforme o nome de um produto: ')
    p_preco = float(input('Informe o preço do produto: R$ '))
    valor_tot += p_preco
    if (p_preco > 1000):
        p_caro += 1
    if (cont == 1):
        p_barato = p_nome
        p_preco_aux = p_preco
    elif (p_preco < p_preco_aux):
        p_preco_aux = p_preco
        p_barato = p_nome
    escolha = input('\nVocê deseja cadastrar outros produtos? [N] Não [Qualquer tecla] Continuar.. ').strip().upper()
    if (escolha == 'N'):
        print('\nOk! Processando informações...')
        break
print(f'Total da compra: R$ {valor_tot}\n{p_caro} produto(s) custou(aram) mais de R$ 1000,00\nProduto mais barato: {p_barato}')