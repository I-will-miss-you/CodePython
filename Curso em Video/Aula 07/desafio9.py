#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
aumento = 15
salario = float(input('Salário: '))
print('Salário final com {0}% de aumento = {1:.2f}'.format(aumento, salario + salario*(aumento/100)))
