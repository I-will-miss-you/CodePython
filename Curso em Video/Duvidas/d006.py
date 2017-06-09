#Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa
#Após isso, o programa irá perguntar o nome de todas elas e colocar numa lista de convidados.
#Após isso irá imprimir todos os nomes da lista.

x = int(input('Quantas pessoas serão convidadas para sua festa? '))  # x = número de pessoas
lista = []

for i in range(0, x):
    lista.append(input('Coloque o nome do convidado #{}: '.format(i + 1)))

print('{:=^35}'.format('Lista de convidados'))
for convidado in lista:
    print(convidado)
