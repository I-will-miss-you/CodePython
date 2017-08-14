from builtins import range


def separador():
    print('\n', '« = »' * 10, '\n')


nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']

'''
# print(nomes)
# print(nomes[0])

for nome in nomes:
    print(nome)
'''

'''
separador()

lista_de_numeros = range(5)
print(lista_de_numeros)
for i in lista_de_numeros:
    print(i)

separador()

lista_de_numeros = range(5, 10)
print(lista_de_numeros)
for i in lista_de_numeros:
    print(i)

separador()

lista_de_numeros = range(0, 100, 2)
print(lista_de_numeros)
for i in lista_de_numeros:
    print(i)
'''

'''
for i in range(4):
    print(nomes[i])
separador()
for i in range(len(nomes)):
    print(nomes[i])

separador()
for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('OII')

print(nomes)
'''

'''
palavra = 'Guilherme Junqueira'
for letra in palavra:
    print(letra)
'''

'''
i = 0
while i < 10:
    print('i ainda é menor que 10: ', i)
    i += 1
print('Acabou o while: ', i)
'''

lista_frutas = ['maça', 'pera', 'uva', 'abacaxi', 'goiaba']

'''
contador = 0
for fruta in lista_frutas:
    contador += 1
print(contador)
'''

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
print('Saiu do while')
