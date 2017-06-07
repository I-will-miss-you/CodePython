# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
a = int(input("Tabuada do: "))
for i in range(1, 10):
    print("{0} * {1} = {2:02}".format(a, i, a * i))
