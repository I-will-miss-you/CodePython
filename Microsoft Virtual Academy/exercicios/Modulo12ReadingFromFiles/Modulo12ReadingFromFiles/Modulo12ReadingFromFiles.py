import csv

fileName = "GuestList.txt"
accessMode = "r"

#Leitura do ficheiro
with open(fileName, accessMode) as myCSVFile:

    dataFromFile = csv.reader(myCSVFile, delimiter =",")

    for row in dataFromFile :
        #print(row) 
        print (', '.join(row))
        for value in row :
            print(value )


#Close
myCSVFile.close()