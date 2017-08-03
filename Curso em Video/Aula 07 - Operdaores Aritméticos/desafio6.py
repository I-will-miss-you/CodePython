# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere: US$1,00 = R$3,27
r = float(input('Valor de R$ em carteira: '))
print("Pode comprar US${0:.3}".format(r / 3.27))
