from math import pow


def é_hipotenusa(h):
    for c1 in range(1, h):
        for c2 in range(1, h):
            if pow(h, 2) == pow(c1, 2) + pow(c2, 2):
                return True
    return False


def soma_hipotenusas(n):
    if n < 5:
        return 0
    soma = 0
    for i in range(5, n + 1):
        if é_hipotenusa(i):
            soma += i
    return soma


print(soma_hipotenusas(25))
