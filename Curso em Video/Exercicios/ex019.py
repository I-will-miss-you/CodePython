# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
