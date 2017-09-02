linha = 1
while linha <= 10:
    print("\nTabuada do {}".format(linha))
    coluna = 1
    while coluna <= 10:
        print("{:2} x {:2} = {:2} ".format(linha, coluna, linha * coluna))
        coluna += 1
    linha += 1
