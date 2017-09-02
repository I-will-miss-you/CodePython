def maximo_2(x, y):
    return x if x > y else y


def maximo(x, y, z):
    return(maximo_2(maximo_2(x, y), z))


print(maximo(30, 14, 10))
print(maximo(0, -1, 1))
