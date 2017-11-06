"""A Confederação Nacional de Natação precisa de um programa que leia o 
ano de nascimento de atleta e mostre sua categoria, de acordo com 
a idade:

- Até  9 anos:  MIRIM
- Até 14 anos:  INFANTIL
- Até 19 anos:  JUNIOR
- Até 20 anos:  SÊNIOR
- Acima:        MASTER 
"""
from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta te {} anos. '.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Clasiificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')