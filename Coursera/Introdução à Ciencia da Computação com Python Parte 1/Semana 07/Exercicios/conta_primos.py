def isPrime(num):
    for n in range(2, num//2 + 1):
        if num % n == 0:
            return False
    return True


def n_primos(num):
    contador = 0
    for n in range(2, num + 1):
        if isPrime(n):
            contador += 1
    return contador
