import turtle

#Variaveis
cor = "red"
comprimento = 0
angulo = 0

#Leitura de valores
comprimento = int(input("Comprimento de linha:"))
cor = input("Escolha uma cor para a linha (black, red, blue, green):")
angulo = int(input("Angulo de rotacao:"))

#desenho
while comprimento != 0:
    turtle.color(cor)
    turtle.right(angulo)
    turtle.forward(comprimento)

    comprimento = int(input("Comprimento de linha: "))
    if comprimento :
        cor = input("Escolha uma cor para a linha (black, red, blue, green): ")
        angulo = int(input("Angulo de rotacao: "))

print("THE END")