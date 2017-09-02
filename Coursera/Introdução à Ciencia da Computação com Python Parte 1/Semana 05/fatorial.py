def fatorial(n):
    fat = 1
    while (n > 1):
        fat *= n
        n -= 1
    return fat


def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))


# TESTES
def testa(num, prev, resultado):
    print(f"Funciona para {num}" if prev ==
          resultado else f"Não funciona para {num}")


def testa_fatorial():
    testa(1, 1, fatorial(1))
    testa(2, 2, fatorial(2))
    testa(0, 1, fatorial(0))
    testa(5, 120, fatorial(5))


def testa_binomial():
    testa({'n': 5, 'k': 3}, 10, numero_binomial(5, 3))
    testa({'n': 20, 'k': 10}, 184756, numero_binomial(20, 10))


testa_fatorial()
testa_binomial()
