'''
Desafio 053

Crie um programa que leia um frase qualquer e 
diga se ela é um palindromo, desconsiderando os espaços.
'''
from unicodedata import normalize 

frase1 = str(input('Digite uma frase: ')).replace(' ','').replace("'", "").upper()
frase1 = normalize('NFD', frase1).encode('ASCII', 'ignore').decode()
frase2 = frase1[::-1]

if frase1 == frase2:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')