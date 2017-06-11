matriz = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']
marcador = False
vitoria = False
referencia = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ' ']]
num = 0
linha = 0
coluna = 0
c = 0
l = 0

import random

def main():
    gerar_matriz()
    while vitoria==False:
        trocar_numeros()
        verificar_vitoria()

def gerar_matriz():
    for li in range(1,5):
        lista=[]
        for co in range(1,5):
            n=random.choice(numeros)
            lista.append(n)
            numeros.remove(n)
        matriz.append(lista)
    for li in matriz:
        for co in li:
            print('{:<3} |'.format(co), end=" ")
        print('\n')


def trocar_numeros():
    global marcador, num, linha, coluna, c, l
    validar_jogada()

    matriz[l][c] = matriz[linha][coluna]
    matriz[linha][coluna] = ' '

    for lista in matriz:
        for co in lista:
            print('{:<3} |'.format(co), end=" ")
        print('\n')



def validar_jogada():
    global marcador, num, linha, coluna, c, l
    marcador=False
    while marcador==False:

        while True:
            try:
                num = int(input('Digite o valor a ser movimentado: '))
                break
            except ValueError as error:
                print('Valor inválido! Digite novamente!')


        for lista in matriz:
            for col in lista:
                if col==num:
                    linha=matriz.index(lista)
                    coluna=lista.index(col)
        for lista in matriz:
            for col in lista:
                if col==' ':
                    l=matriz.index(lista)
                    c=lista.index(col)
        if linha==l and coluna==(c+1):
            marcador=True
        elif linha==l and coluna==(c-1):
            marcador=True
        elif linha==(l+1) and coluna==c:
            marcador=True
        elif linha==(l-1) and coluna==c:
            marcador=True
        else:
            print('Movimento inválido!')


def verificar_vitoria():
    global vitoria
    vitoria=False
    if matriz==referencia:
        vitoria=True
        print('Vitória!')
    else:
        vitoria=False

main()
