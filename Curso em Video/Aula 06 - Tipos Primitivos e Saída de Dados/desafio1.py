# Crie um programa que leia dois números e mostre a soma entre eles
isnum = False
while isnum != True:
    a = input("Valor 1: ")
    b = input("Valor 2: ")
    isnum = a.isnumeric() & b.isnumeric();
    if isnum == False:
        print("Ambos os valores têm de ser númericos...")

s = float(a) + float(b)
print('{0} + {1} = {2}'.format(a, b, s))
