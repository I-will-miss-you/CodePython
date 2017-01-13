import sys

#Variáveis
filename = " "
fileContents = " "

#Entrada de dados
filename = input("Informe o nome do ficheiro: ")
filename +=".txt" 
#Acessar o ficehiro
try:
    myFile = open(filename,'r')
    fileFound = True

except FileNotFoundError :
    print("O ficheiro " + filename + " nao encontrado.")
    fileFound = False

except :
    error = sys.exc_info()
    print(error)
    fileFound = False

#Se o arquivo for aberto com sucesso: ler e exibir o conteúdo do ficheiro
if fileFound :
    fileContents = myFile.read()
    print(fileContents)

