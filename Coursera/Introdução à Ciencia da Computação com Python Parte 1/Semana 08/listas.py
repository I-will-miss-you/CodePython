def éPrimo(x):
    if(x == 2):
        return True
    fator = 2
    while x % fator != 0 and fator <= x / 2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


def primos(n):
    lista = []
    for n in range(2, n):
        if éPrimo(n):
            lista.append(n)
    return lista


lista_primos = primos(100)

print("Lista inicial")
print(lista_primos)

# sub lista
print(lista_primos[1:7])
print(lista_primos[:7])
print(lista_primos[7:])

#Clonar lista
lista2 = lista_primos[:]
lista2[0] = 2000
print(lista2)