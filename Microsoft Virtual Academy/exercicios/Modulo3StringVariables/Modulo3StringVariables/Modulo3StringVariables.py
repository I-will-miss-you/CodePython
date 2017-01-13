
#initialize the variables
animalGrande = " "
animalPequeno = " "
somAnimal = " "
ativivade = " "

animalGrande = input("Escolher um animal de grande porte (Raposa, Leao, Girafa, ...): ")
somAnimal = input("Som que o animal de grande porte faz (Latir, Uivar, Rugido, ...): ")
animalPequeno = input("Escolher um animal de pequeno porte (Ratinho, Sardaozinho, ...): ")
atividade = input("Ecolher uma atividade (cacar, correr, ...): ")




#Display the story
print("")
print("Um " + animalGrande.capitalize() + " cansado de tanto " + atividade.lower() + ", dormia espichado a sombra de uma boa arvore. ")
print("Vieram uns " + animalPequeno.capitalize() + "s passear em cima dele e ele acordou.\
 \nTodos conseguiram fugir, menos um, que o " + animalGrande.capitalize() + " prendeu embaixo da pata.")
print("Tanto o " + animalPequeno.capitalize() + " pediu e implorou que o " + animalGrande.capitalize() + " desistiu de esmaga-lo e deixou que fosse embora.")
print("Algum tempo depois, o " + animalGrande.capitalize() + " ficou preso na rede de uns cacadores.")
print("Nao conseguia se soltar, e fazia a floresta inteira tremer com seu " + somAnimal.lower() + " de raiva.")
print("Nisso, apareceu o " + animalPequeno.capitalize() + ". Com seus dentes afiados, roeu as cordas e soltou o " + animalGrande.capitalize() + ".")
print("FIM!!! \n\n")