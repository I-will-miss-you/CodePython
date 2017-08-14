'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela apta a ser do Exercito.
Para entrar no Exercito é preciso:
 - ter mais ou igual de 18 anos
 - pesar mais ou igual de 60 kilos
 - medir mais ou igual de 1.70 metros
'''
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

if(idade >= 18 and peso >= 60 and altura >= 1.70):
    print('Você esta apto a entrar no exercito')
else:
    print('Você não esta apto a entrar no exercito')
