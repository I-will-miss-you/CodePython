#gambiarra a tuga:

chamadas = -1
def fib(n):
    global chamadas
    chamadas += 1
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    if n == 0 or n == 1:
        global chamadas
        chamadas = 1
        return n
    else:
        return fib(n)


x = int(input('Insira um numero: '))
print('Fibonacci: {}\nIterações: {}'.format(fibonacci(x),chamadas))

