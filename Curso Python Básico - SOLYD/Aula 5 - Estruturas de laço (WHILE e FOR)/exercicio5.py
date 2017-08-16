'''
    EXERCICIO: Faça um programa que leia quantidade de pessoas que serão convidadas para uma festa.
    O programa irá perguntar o nome de todas as pessoas e colcar num lista de convidados.
    Após isso deve imprimir todos os nomes da lista
'''

'''
qtd = int(input("Quantas pessoas vão ser convidadas?"))

lista_pessoas = []

while qtd > 0:
    lista_pessoas.append(input('Nome: '))
    qtd -= 1

for pessoa in lista_pessoas:
    print(pessoa)
'''

# Resolução do exercício
print('Programinha de controle de festinhas 1.0')
print('#' * 20)

numero_de_convidados = int(input('Coloque o número de convidados: '))
lista_de_convidados =[]

i = 1
while i <= numero_de_convidados:
    nome_do_convidado = input('Coloque o nome do convidado #' + str(i) + ': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('Serão ', numero_de_convidados, 'convidados')
print('\nLISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)

