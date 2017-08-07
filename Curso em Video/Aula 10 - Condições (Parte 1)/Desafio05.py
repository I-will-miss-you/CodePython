#Faça um programa que leia um ano qualquier e mostre se ele é BISSEXTO.

year = int(input('Ano: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('{} é um ano Bissexto!'.format(year))
else:
    print('{} não é um ano Bissexto!'.format(year))