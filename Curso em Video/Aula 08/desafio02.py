# Faça um programa que leia o comprimento do cateto adjacente de
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

ca = float(input('Cateto adjacente? '))
co = float(input('Cateto oposto? '))

# Usado o Teorema de Pitágoras
from math import pow, sqrt

print('Hipotenusa = {:.2f}'.format(sqrt(pow(ca, 2) + pow(co, 2))))

# Usando a função hypo()
from math import hypot

print('Hipotenusa = {:.2f}'.format(hypot(ca, co)))
