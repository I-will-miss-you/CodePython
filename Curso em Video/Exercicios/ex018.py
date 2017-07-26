# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tagente desse ângulo
from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2} '.format(ângulo, seno))

cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSENO de {:.2} '.format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print('O ângulo de {} tem o TANGENTE de {:.2} '.format(ângulo, tangente))
