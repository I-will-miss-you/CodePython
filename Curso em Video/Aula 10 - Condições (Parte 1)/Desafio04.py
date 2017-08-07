# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$050 por Km para viagens
# de até 200km e R$0.45 para viagens mais longas.

distance = int(input("Distância em KM: "))

valor = 0.5 * distance if distance <= 200 else 0.45 * distance
print('Preço da passagem = R${:.2f}'.format(valor))
