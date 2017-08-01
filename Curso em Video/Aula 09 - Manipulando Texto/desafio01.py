# Crie um programa que leia um nome completo de uam pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas minúsculas
# 3 - Quantas letras (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = input("Nome:").strip()
nomes = nome.split()

# nome em maiúsculas
print(nome.upper())

# nome em minúsculas
print(nome.lower())

# nº de letras
print(len(nome.replace(" ","")))

#nº letras do primeiro nome
print(len(nomes[0]))

