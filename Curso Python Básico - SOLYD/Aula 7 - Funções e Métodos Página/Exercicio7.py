'''
    EXERCICIO: Escreva um função que recebe um objeto de coleção
    e retorna o valor do maior numero dentro dessa coleção e outra
    que retorne o menor
'''


def maior(colecao):
    maior = colecao[0]
    for item in colecao:
        if maior < item:
            maior = item
    return maior


def menor(colecao):
    menor = colecao[0]
    for item in colecao:
        if menor > item:
            menor = item
    return menor


lista = [54, 20, 13, 4, 145, 62, 79, 8, 9]
print('Maior: {}'.format(maior(lista)))
print('Menor: {}'.format(menor(lista)))