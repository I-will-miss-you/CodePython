# Desafio 007
# Desenvolva um programa que leia as duas notas de um aluno, clcule e mostre a sua média

n1 = float(input('Primeira nota de aluno: '))
n2 = float(input('Segunda nota do aluno: '))

#Forma errada
#média = n1 + n2 / 2

#Forma correta
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))