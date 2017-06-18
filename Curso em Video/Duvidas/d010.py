#Proposta 4:
#Escreva um programa para calcular o tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e
#  por quantos anos ele fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias
# de vida um fumante perderá. Exiba o total em dias.

qtdCigarros = int(input('Quantidade de cigarros fumados por dia: '))
qtdAnosFumou = int(input('Quantos anos ele fumou: '))

vidaPerdida = 10 * qtdCigarros * 365 * qtdAnosFumou #minutos perdidos

diasPerdidos = vidaPerdida / (24 * 60)

print("Você já perdeu {:.0f} dias de vida".format(diasPerdidos))

