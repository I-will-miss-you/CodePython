
#Variaveis
list = []
i = 0
numeroConvidaddos = 0

#Entrada de valores
#tamanho da lista
numeroConvidaddos = int(input("Numero de convidados na lista: "))

#Inserir os nomes na lista 
for x in range(0,numeroConvidaddos):
    list.append(input("Nome:"))

#ordenar a lista 
list.sort() #ordena de forma crescente
#list.reverse() #inverte a lista

for x in list:
    print(x)    
    

