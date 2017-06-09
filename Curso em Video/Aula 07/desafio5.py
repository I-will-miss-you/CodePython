# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
a = int(input("Tabuada do: "))
for i in range(1, 11):
    print("{0} * {1} = {2:02}".format(a, i, a * i))

print('{:=^30}'.format("Sem o ciclo For"))

print("{0} * 1  = {1:02}".format(a, a * 1))
print("{0} * 2  = {1:02}".format(a, a * 2))
print("{0} * 3  = {1:02}".format(a, a * 3))
print("{0} * 4  = {1:02}".format(a, a * 4))
print("{0} * 5  = {1:02}".format(a, a * 5))
print("{0} * 6  = {1:02}".format(a, a * 6))
print("{0} * 7  = {1:02}".format(a, a * 7))
print("{0} * 8  = {1:02}".format(a, a * 8))
print("{0} * 9  = {1:02}".format(a, a * 9))
print("{0} * 10 = {1:02}".format(a, a * 10))
