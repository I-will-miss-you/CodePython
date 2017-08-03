# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

# ver: https://docs.python.org/3/library/random.html?highlight=shuffle
deck = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(deck)

print(deck[0])
print(deck[1])
print(deck[2])
print(deck[3])

# Mais uma maneira de fazer, mas agora usando um array
alunos = []
for i in range(4):
    alunos.append(input('Nome do aluno {}: '.format(i + 1)))

random.shuffle(alunos)
for i in range(4):
    print(alunos[i])
