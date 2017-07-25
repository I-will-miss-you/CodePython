# Faça um programa que leia o comprimento do cateto adjacente de
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Comprimento do cateto oposto? '))
ca = float(input('Comprimento do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))


# Usando a função hypo() da biblioteca math
hi2 = hypot(co, ca)
print('Hipotenusa = {:.2f}'.format(hi2))
