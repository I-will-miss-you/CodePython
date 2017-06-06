# Desafio 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possiveis sobre ele.

a = input("Escreva algo: ")

print('O tipo primitivo: {}.'.format(type(a)))
print('Só tem espaços? {}.'.format(a.isspace()))
print('É um número? {}.'.format(a.isnumeric()))
print('É alfabético? {}.'.format(a.isalpha()))
print('É alfanúmerico? {}.'.format(a.isalnum()))
print('Está em maiúsculas? {}.'.format(a.isupper()))
print('Está em minúsculas? {}.'.format(a.islower()))
print('Está capitalizada? {}.'.format(a.istitle()))

