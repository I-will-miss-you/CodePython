def isPrime(n):
    if(n <= 0):
        return None
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def maior_primo(n):
    while( n > 2):
        if isPrime(n):
            return n
        n -= 1
    return None


def test_answer():
    assert isPrime(7) == True
    assert isPrime(97) == True
    assert isPrime(8) == False
    assert isPrime(0) == None
    assert maior_primo(100) == 97
    assert maior_primo(7) == 7