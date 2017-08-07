
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir quel foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

secret_number = random.randint(0, 5)
user_number = int(input('Escolha um número entre 0 e 5: '))

mensagem = 'Parabéns, você acertou!' \
               if secret_number == user_number \
               else 'Oooh :(, você perdeu. O número secreto era {}'.format(secret_number)

print(mensagem)

