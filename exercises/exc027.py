# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza
nome = input('Digite o seu nome completo: ').strip()
print('O primeiro nome é "{}"'.format(nome.split()[0]))
print('O último nome é "{}"'.format(nome.split()[-1]))