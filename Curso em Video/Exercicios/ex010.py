# Desafio 010
# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere: US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
