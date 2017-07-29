import math
#esta forma esta errada
print('Fórmula de Bhaskara')

a = int(input('\nDigite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

x = (b ** 2) - (4 * a * c)

x1 = (- b + math.sqrt(x)) / (2 * a)
x2 = (- b - math.sqrt(x)) / (2 * a)

if x < 0:
    print('Esta equação não possui raízes Reais.')
elif x == 0:
    print('A raiz dessa equação é {}'.format(x1))
else:
    print('\nValor de x1 {} \nValor de x2 {}'.format(x1, x2))