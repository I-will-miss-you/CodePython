#Calculador - Peso Ideal
sair = False

while (sair == False):

    # Leitura dos dados do utilizador
    altura = float(input('Quanto mede em Metros? '))
    peso = float(input('Quanto pesa em Kg?'))
    sexo = input('Qual seu sexo?[F/M] ').lower()


    if (sexo == 'm' or sexo == 'f'):
        # calcular o peso ideal
        if (sexo == 'f'):
            pesoIdeal = (72.7 * altura) - 58
        elif (sexo == 'm'):
            pesoIdeal = (62.1 * altura) - 44.7

        # imprime  o resultado
        if (peso > pesoIdeal):
            print('Voce está acima do peso ideal, deveria pesar {:.2f}'.format(pesoIdeal))
        elif (peso < pesoIdeal):
            print('VOce está abaixo do peso ideal, deveria pesar {:.2f}'.format(pesoIdeal))
        else:
            print('Voce tem o peso ideal! Parabéns')
            print('O seu peso ideal é {:.2f}'.format(pesoIdeal))

    # caso não seja 'm' ou 'f'
    else:
        print("Você inseriu dados invalidos")

    # valida se quer sair ou não
    op = input("Clique \'Enter\' para continuar ou digite \'s\' para sair:\n ").lower()
    if (op == 's'):
        sair = True
        print("Obrigado e volte sempre... :-p")
