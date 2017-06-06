# Faça um programa que leia algo pelo teclado e mostra na tela o
# seu tipo primitivo e todas as informações possiveis sobre ele.


print("Escreva...")
a = input("$:\> ")
print("Tipo primitivo: ", type(a))
print("É número [0-9]: ", a.isnumeric())
print("É alfa [a-zA-Z]", a.isalpha())
print("É alfa númerico [a-zA-Z0-9]", a.isalpha())

