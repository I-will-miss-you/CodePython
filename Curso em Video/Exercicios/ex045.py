'''
Crie um programa que faça o computador
jogar Jokenpô com você
'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

jogador = int(input('Qual é a sua jogada? '))

print()
print(f"{'JO':^60}")
sleep(1)
print(f"{'KEN':^60}")
sleep(1)
print(f"{'PO!!!':^60}")

erro = False
if computador == 0:
    if jogador == 0:
        resultado = 'Empate'
    elif jogador == 1:
        resultado = 'Jogador Vence'
    elif jogador == 2:
        resultado = 'Computador Vence'
    else:
        erro = True
elif computador == 1:
    if jogador == 0:
        resultado = 'Computador Vence'
    elif jogador == 1:
        resultado = 'Empate'
    elif jogador == 2:
        resultado = 'Jogador Vence'
    else:
        erro = True
elif computador == 2:
    if jogador == 0:
        resultado = 'Jogador Vence'
    elif jogador == 1:
        resultado = 'Computador Vence'
    elif jogador == 2:
        resultado = 'Empate'
    else:
        erro = True


if erro:
    print('JOGADA INVÁLIDA')
else:
    print(f"\n\n{'-='*20:^60}")
    print(f"{f'Computador jogou: {itens[computador]}':^60}")
    print(f"{f'   Jogador jogou: {itens[jogador]}':^60}")
    print(f"\n{resultado:^60}")
    print(f"{'-='*20:^60}")
