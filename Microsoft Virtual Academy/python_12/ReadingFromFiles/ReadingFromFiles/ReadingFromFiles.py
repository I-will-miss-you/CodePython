import csv

with open ("Tasmania.txt","r") as animalFile:
    #allRowsList = csv.reader(animalFile) #default delimiter=","
    allRowsList = csv.reader(animalFile, delimiter=";")

    for currentRow in allRowsList :
        #print(currentRow)
        print(' -> '.join(currentRow))
        #for currentWord in currentRow :
        #    print(currentWord)




##Open my file
#animalFile = open("Tasmania.txt","r")

#firstAnimal = animalFile.readline()
#print(firstAnimal)
#secondAnimal = animalFile.readline()
#print(secondAnimal)

##read all files contents
#allFileContents = animalFile.read()
#print(allFileContents)