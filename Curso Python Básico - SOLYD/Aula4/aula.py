
frase = 'Oi, tudo bem?'

lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

#print(type(lista_nomes))

#print(lista_nomes[0])
#print(lista_nomes)

#print(frase[3:10])
#print(frase[2:13:2])

#print(lista_nomes[0:4])
#print(lista_nomes[0:4:2])

#print(lista_nomes[-1])
#print(lista_nomes[-3])

#print(lista_nomes[-1:-5:-1])

#print(frase[::-1])


### Adiciona um valor a lista
lista_nomes.append('Geralda')
print(lista_nomes)
lista_nomes.append('Lorena')
print(lista_nomes)
lista_nomes.append('João')

### Insere um novo valor numa dada posição
lista_nomes.insert(1,'Creosvaldo')
print(lista_nomes)

### Muda o valor contido
#lista_nomes[0] = 'Robervania'
#print(lista_nomes)

### Remove um elemento da lista
#lista_nomes.remove('João')
#print(lista_nomes)

### Remove todos os elementos da lista
#lista_nomes.clear()
#print(lista_nomes)

### Contar o número em que um dado valor existe
#contador_joao = lista_nomes.count('João')
#print(contador_joao)

### Tamanho de uma String
#print(len(frase))

### Tamanho de uma Lista
#print(len(lista_nomes))

### Retorna o "ultimo" elemento da lista removendo-o da mesma
#print(lista_nomes.pop())
#print(lista_nomes)
#print(lista_nomes.pop())
#print(lista_nomes)

### converter todos os caracteres de uma string para minusculas
print(frase.lower())

### converter todos os caracteres de uma string para maiusculas
print(frase.upper())

### "Capitalize" de uma string
print(frase.capitalize())

### Converter uma String numa Lista de Strings
frase_separada = frase.split(',')
print(frase_separada)

### Concatenar
frase_nova = frase + 'Como vai você?'
print(frase_nova)



