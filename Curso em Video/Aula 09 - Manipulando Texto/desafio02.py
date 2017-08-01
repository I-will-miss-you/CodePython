# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena:  3
# Centena: 8
# milhar:  1

num = input('Digite um número de 4 algarismos [0000 - 9999]: ')
print("unidade: " + num[3])
print("dezena : " + num[2])
print("centena: " + num[1])
print("milhar : " + num[0])

# Matematicamente
n = int(input('Digite um número de 4 algarismos [0000 - 9999]: '))
print(n % 10)
n = int(n / 10)
print(n % 10)
n = int(n / 10)
print(n % 10)
n = int(n / 10)
print(n)
