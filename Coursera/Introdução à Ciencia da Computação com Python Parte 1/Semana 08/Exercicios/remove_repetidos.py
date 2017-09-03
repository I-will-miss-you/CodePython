def remove_repetidos(lista):
    list_aux = []
    for l in lista:
        if l not in list_aux:
            list_aux.append(l)
    list_aux.sort()
    return list_aux

