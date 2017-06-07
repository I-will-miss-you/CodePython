#Faça um algoritmo que leia um preço de um produto e mostre seu preço, com 5% de desconto.
desc = 5
preco = float(input('Preço: '))
print('Preço final com {0}% de desconto = {1:.2f}'.format(desc, preco - preco*(desc/100)))
