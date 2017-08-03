# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura*altura
print("Área = {0:.2f}".format(area))
print("Tinta necessária = {0} lt".format(area/2 + 1))

