# Crie um programa que leia um nome completo de uam pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas minúsculas
# 3 - Quantas letras (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
