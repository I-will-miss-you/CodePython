#Cria um programa que  leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num,trunc(num)))

# usando a função int()
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
