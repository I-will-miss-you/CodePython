print("Calculadora em Python")

num1 = int(input('valor 1: '))
num2 = int(input('valor 2: '))
operador = input("operador: ")
if operador == '+':
    print('{0} + {1} = {2}'.format(num1, num2, num1 + num2))
elif operador == '-':
    print('{0} - {1} = {2}'.format(num1, num2, num1 - num2))
elif operador == '*':
    print('{0} * {1} = {2}'.format(num1, num2, num1 * num2))
elif operador == '/':
    print('{0} / {1} = {2}'.format(num1, num2, num1 / num2))
else:
    print("opção invalida")
