# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
number = int(input('Número: '))
print('O número {} é {}'.format(number, 'PAR' if number % 2 == 0 else 'ÍMPAR'))
