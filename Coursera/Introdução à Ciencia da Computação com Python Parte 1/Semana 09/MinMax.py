def MinMax(temperaturas):
    print("A menor temperatura do mês foi: {} C.".format(mínima(temperaturas)))
    print("A maior temperatura do mês foi: {} C.".format(máxima(temperaturas)))


def mínima(temperaturas):
    min = temperaturas[0]
    for temp in temperaturas:
        if min > temp:
            min = temp
    return min


def máxima(temperaturas):
    max = temperaturas[0]
    for temp in temperaturas:
        if max < temp:
            max = temp
    return max

##############################################################
#   TESTES      TESTES      TESTES      TESTES      TESTES   #
##############################################################
def teste(temps, min, max):
    info = '\033[34m'
    clear = '\033[m'

    sucesso = "\033[32m" + "Sucesso" + clear
    erro = "\033[31m" + "Erro" + clear

    print(info + "\nTemperaturas para teste:" + clear)
    print("\033[33m {} \033[m".format(temps))

    print(info + "Teste mínima:" + clear)
    min_obt = mínima(temps)
    print("valor esperado: {} valor obtido {} --» {}".format(min,
                                                             min_obt, sucesso if min == min_obt else erro))
    print(info + "Teste máxima:" + clear)
    max_obt = máxima(temps)
    print("valor esperado: {} valor obtido {} --» {}".format(max,
                                                             max_obt, sucesso if max == max_obt else erro))


def lista_de_testes():
    title = '\033[7m'
    clear = '\033[m'
    print(title + "Iniciar testes" + clear)
    temp = [0]
    teste(temp, 0, 0)

    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    teste(temp, 0, 0)

    temp = [30, 31, 35, 25, 26, 27, 34, 35, 29,
            27, 28, 29, 24, 23, 22, 25, 26, 27, 28, 30]
    teste(temp, 22, 35)

    temp = [30, 31, 35, -2, 26, 27, -4, 35, 29, -
            7, 28, 29, 24, 23, 22, 25, -6, 27, -8, 30]
    teste(temp, -8, 35)

    print(title + "Teste finalizado" + clear)


lista_de_testes()
