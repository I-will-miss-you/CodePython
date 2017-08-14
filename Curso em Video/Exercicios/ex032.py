#Faça um programa que leia um ano qualquier e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano quer sanalisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} Não é BISSEXTO'.format(ano))

