'''
Desafio 053

Crie um programa que leia um frase qualquer e 
diga se ela é um palindromo, desconsiderando os espaços.
'''
from unicodedata import normalize 

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

'''
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''

inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')