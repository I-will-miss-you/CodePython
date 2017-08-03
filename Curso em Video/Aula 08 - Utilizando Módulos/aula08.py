"""
import math

i = 4.65

#Arredomdamento para cima
print(math.ceil(i))

#Arredomdamento para baixo
print(math.floor(i))

#truncar, eleiminar valor após a virgula
print(math.trunc(i))

#potência
print(math.pow(i,2))

#rais quadrada
print(math.sqrt(i))

#fatorial
print(math.factorial(5))
"""

"""
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num);
print('A raiz de {} é gual a {:.2f}'.format(num, raiz))
"""

"""
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num);
print('A raiz de {} é gual a {:.2f}'.format(num, floor(raiz)))
"""

"""
import random

num = random.random()
numInt = random.randint(1,10)
print(num)
print(numInt)
"""

import emoji

print(emoji.emojize("Olá, Mundo :smile:", use_aliases=True))
