# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tagente desse ângulo
from math import sin, cos, tan, radians

ang = float(input('Ângulo em graus = '))
rad = radians(ang)

print('Cosseno = {:.2f}'.format(cos(rad)))
print('Seno = {:.2f}'.format(sin(rad)))
print('Tangente = {:.2f}'.format(tan(rad)))
