matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turno = True  # Marcador de seleção de turno
l = 0  # Input linha
c = 0  # Input coluna
player1 = " "  # Nome do Jogador 1
player2 = " "  # Nome do Jogador 2
vitória = False  # Marcador de vitória e fim do jogo

import os
import random


def TelaJogo():
    global matriz
    os.system('cls')
    print('')
    for linha in matriz:
        print('|', end=' ')
        for coluna in linha:
            print('{:^3} |'.format(coluna), end=" ")
            print('\n' + '-' * 19)


def player_1():
    global matriz, l, c, player1
    print('Turno do(a) {}'.format(player1))
    validar_jogada()
    matriz[l - 1][c - 1] = 'X'


def player_2():
    global matriz, l, c, player2
    print('Turno do(a) {}'.format(player2))
    validar_jogada()
    matriz[l - 1][c - 1] = 'O'


def validar_jogada():
    global l, c
    while True:
        try:
            l = int(input('Digite a linha: '))
            c = int(input('Digite a coluna: '))
            break
        except ValueError:
            print('JOGADA NÃO VÁLIDA! SOMENTE NÚMEROS INTEIROS DE 1 A 3 SÃO ACEITOS')
    while (l < 1 or l > 3) or (c < 1 or c > 3):
        print('SOMENTE NÚMEROS INTEIROS DE 1 A 3 SÃO VÁLIDOS')
        l = int(input('Digite novamente a linha: '))
        c = int(input('Digite novamente a coluna: '))
    while matriz[l - 1][c - 1] != " ":
        print('JOGADA NÃO VÁLIDA!')
        l = int(input('Digite novamente a linha: '))
        c = int(input('Digite novamente a coluna: '))


def definir_player():
    pl = [True, False]
    turno = random.choice(pl)
    for i in range(1, 10):
        if turno == True:
            player_1()
            TelaJogo()
            turno = not (turno)
        else:
            player_2()
            TelaJogo()
            turno = not (turno)
        verificar_vitória()
        if vitória == True:
            break


def verificar_vitória():
    global vitória
    if (matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0]) and matriz[0][0] != " ":
        if matriz[0][0] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[0][1] == matriz[1][1] and matriz[0][1] == matriz[2][1]) and matriz[0][1] != " ":
        if matriz[0][1] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2]) and matriz[0][2] != " ":
        if matriz[0][2] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2]) and matriz[0][0] != " ":
        if matriz[0][0] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2]) and matriz[1][0] != " ":
        if matriz[1][0] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2]) and matriz[2][0] != " ":
        if matriz[2][0] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2]) and matriz[1][0] != " ":
        if matriz[0][0] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True
    if (matriz[0][2] == matriz[1][1] and matriz[0][2] == matriz[2][0]) and matriz[0][2] != " ":
        if matriz[0][2] == 'X':
            print('VITÓRIA DO(A) {}'.format(player1))
            vitória = True
        else:
            print('VITÓRIA DO(A) {}'.format(player2))
            vitória = True


def main():
    global turno, player1, player2
    TelaJogo()
    player1 = input('Nome do Jogador 1: ')
    player2 = input('Nome do Jogador 2: ')
    definir_player()


main()
