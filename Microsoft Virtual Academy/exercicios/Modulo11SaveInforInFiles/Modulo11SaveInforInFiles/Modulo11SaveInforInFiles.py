#Variaveis
fileName = "GuestList.txt"
accessMode = "w"

#Open the file for writing
myFile = open(fileName, accessMode)

#Guardar informação
myFile.write("Doyle McCarty,27\n")
myFile.write("Jodi Mills,25\n")
myFile.write("Nicholas Rose,32\n")
myFile.write("Kian Goddard,36\n")
myFile.write("Zuha Hanania,26\n")

#receber dados do utilizador
flag = 1
while flag:
    if flag :
        nome = input("Nome: ")
        idade = input("Idade: ")
        myFile.write(nome + "," + idade  + "\n")

    cont = (input("Deseja continuar? press 's' to cont... ")).lower()
    flag = 1 if cont == 's' else 0 #operação ternária
    

#Close
myFile.close()

