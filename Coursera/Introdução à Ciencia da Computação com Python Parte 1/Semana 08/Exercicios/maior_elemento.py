def maior_elemento(lista):
    maior = lista[0]
    for num in lista:
        if maior < num:
            maior = num
    return maior


lista = [1,2,4,5,7,8,4,1,2,5,9]
print(maior_elemento(lista))