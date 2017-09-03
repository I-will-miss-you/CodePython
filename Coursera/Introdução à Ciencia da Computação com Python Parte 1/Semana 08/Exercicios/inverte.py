
lista = []

num = int(input('Digite um número: '))
while(num != 0):
    lista.append(num)
    num = int(input('Digite um número: '))

print()
lista.reverse()
for num in lista:
    print(num)
