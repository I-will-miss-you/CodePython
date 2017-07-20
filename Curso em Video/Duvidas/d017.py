# Por exemplo, o número 41 pode ser representado como (-4)2 + 52 = 41, já o número 7 não pode ser representado da mesma maneira.
# Entrada
# A entrada é composta por várias linhas, cada linha contém um inteiro com módulo menor ou igual a 10000.
# Saída
# Para cada linha, imprima "YES" se o número pode ser representado por uma soma de dois inteiros ao quadrado, caso contrário imprima "NO".


num = int(input("Num: "))
soma = 0
for i in range(int(num/2)):
    for j in range(int(num/2)):
        soma = i ** 2 + j ** 2
        if (soma >= num):
            break
    if (soma == num):
        print("{0}^2 + {1}^2 = {2}".format(i, j, num))
        break
