# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome) - 1]))
