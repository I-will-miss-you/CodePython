import turtle

#variaveis
lados = 0
comprimentoLinha = 100

#entrada de valores
lados = int(input("Numero de lados:"))

#desenho
for lado in range(0,lados) :
    turtle.forward(comprimentoLinha)
    turtle.right(360 / lados)

    for lado in range(0,lados) :
        turtle.forward(comprimentoLinha / 3)
        turtle.right(360/lados)

