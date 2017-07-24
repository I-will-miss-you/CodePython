# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from _ctypes import Array
from random import randint

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

n = randint(1, 4)
if (n == 1):
    print(aluno1)
elif (n == 2):
    print(aluno2)
elif (n == 3):
    print(aluno3)
elif (n == 4):
    print(aluno4)
else:
    print("O professor apaga... :)")


# Mais uma maneira, usando um array
alunos = []
for i in range(4):
    alunos.append(input('Nome do aluno {}: ' .format(i + 1)))

n = randint(0, 3)
print(alunos[n])
