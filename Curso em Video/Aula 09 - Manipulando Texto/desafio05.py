# Faça umprograma que leia um frase pelo teclado e mostre:
#  Quantas vezes aparece a letra "A"
#  Em que posição ela aparece a primeira vez
#  Em que posição ela aparece a última vez
frase = input("Frase: ")
print("Quantas vezes aparece a letra \"A\": {}".format(frase.count("A")))
print("Em que posição ela aparece a primeira vez: {}".format(frase.find("A")))
print("Em que posição ela aparece a última vez: {}".format(frase.rfind("A")))
