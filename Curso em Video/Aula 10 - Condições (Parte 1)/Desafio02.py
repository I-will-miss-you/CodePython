# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostra um mensagem dizendo que ele foi multado.
# A multado vai custar R$7,00 por cada km acima do limite.

velocity = int(input('Velocidade: '))

if velocity > 80:
    multa = (velocity - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))