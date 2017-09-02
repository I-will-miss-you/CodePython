def soma(x, y):
    return x + y


def multiplica(x, y, z):
    return x * y * z


def fatorial(x):
    if(x < 0):
        return None
    if(x == 0 or x == 1):
        return 1
    return x * fatorial(x - 1)


print(soma(10, 20))
print(multiplica(-20, 100, soma(10, 25)))
print(fatorial(-9))
