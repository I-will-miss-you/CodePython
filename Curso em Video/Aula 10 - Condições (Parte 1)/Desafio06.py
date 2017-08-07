#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('Número 1: '))
number2 = int(input('Número 2: '))
number3 = int(input('Número 3: '))

if number1 > number2 and number1 > number3:
    maior = number1
    menor = number3 if number2 > number3 else number2

elif number2 > number1 and number2 > number3:
    maior = number2
    menor = number3 if number1 > number3 else number1

else:
    maior = number3
    menor = number2 if number1 > number2 else number1

print('*******************************************')
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))


