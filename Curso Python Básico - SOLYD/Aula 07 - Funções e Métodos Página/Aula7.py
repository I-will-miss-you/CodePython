# Função soma dois números
def soma(numero1, numero2):
    return numero1 + numero2


def print_oi():
    print("OI")


def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False


retorno = soma(75, 1289)
print(retorno)

retorno = soma(12.35, 75.61)
print(retorno)

print_oi()

if tem_sete_itens('1234567'):
    print('Tem sete lettras')

print(tem_sete_itens({1, 2, 3, 4, 5, 6, 7}))
print(tem_sete_itens({1, 2, 3, 4, 5, 6, 7, 8}))