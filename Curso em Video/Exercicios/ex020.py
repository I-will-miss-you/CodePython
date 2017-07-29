# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)