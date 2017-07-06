# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.2f} lit de tinta.'.format(tinta))

